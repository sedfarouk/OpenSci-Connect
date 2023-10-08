from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User # jango built in model -> allows creation sign up and login view
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import UserProfile, Project, Message, UserProjectInteraction
from .forms import ProjectForm, MessageForm
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import requests # <-- for fetching API's of NASA


#fetch APOD API (Nasa daily pictures)

def fetch_apod():
    url = "https://api.nasa.gov/planetary/apod?api_key=Jbm6MlEtCMeow8EedEFMEcfoXEfd9YmyvhbYdZ2b"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        nasa_apod = NasaAPOD(data['title'], data['url'], data['explanation'])
        return nasa_apod
    else:
        return None

#fetch MArs ROVER API 
def fetch_mars_rover_photos(request):
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=Jbm6MlEtCMeow8EedEFMEcfoXEfd9YmyvhbYdZ2b"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        mars_photos = MarsRoverPhoto(data['photos'])
        return render(request, "mars_photos.html", {'mars_photos':mars_photos})
    else:
        return None


# Fetch rotation of the earth EPIC API
def fetch_epic(request):
    url = "https://api.nasa.gov/EPIC/api/natural/images?api_key=Jbm6MlEtCMeow8EedEFMEcfoXEfd9YmyvhbYdZ2b"  
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return render(request, "epic.html", {'data':data})
    else:
        return None


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def custom_login(request):
    response = auth_views.LoginView.as_view()(request)
    if request.user.is_authenticated:
        return redirect('user_profile') 
    return response


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('project_list')
    return render(request, 'registration/login.html')


def get_user_project_interactions():
    users = UserProfile.objects.all()
    projects = Project.objects.all()
    
    user_project_matrix = np.zeros((len(users), len(projects)))
    
    for i, user in enumerate(users):
        for j, project in enumerate(projects):
            interaction = UserProjectInteraction.objects.filter(user=user, project=project).first()
            if interaction:
                user_project_matrix[i][j] = 1  
    
    # Remove rows that are all zero
    user_project_matrix = user_project_matrix[~np.all(user_project_matrix == 0, axis=1)]
    
    return users, projects, user_project_matrix

@login_required
def user_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    users, projects, user_project_matrix = get_user_project_interactions()
    
    users = list(users)

    if len(users) < 2 or len(projects) < 2 or user_project_matrix.shape[0] < 1:
        recommended_projects = [] 
    else:
        try:
            svd = TruncatedSVD(n_components=2)
            user_project_matrix_svd = svd.fit_transform(user_project_matrix)

            similarity_matrix = cosine_similarity(user_project_matrix_svd)

            # Protecting against potential IndexError for users
            try:
                user_index = users.index(user_profile)
            except ValueError:
                return render(request, 'user_profile.html', {'user_profile': user_profile, 'recommended_projects': []})

            user_similarities = similarity_matrix[int(user_index)]
            sorted_indices = [int(i) for i in np.argsort(user_similarities)[::-1]]

            recommended_projects = []
            for i in sorted_indices:
                # Add a condition to ensure the index is within the range of 'projects'
                if i < len(projects):
                    if user_project_matrix[i].sum() < 0.1:
                        recommended_projects.append(projects[i])
                    if len(recommended_projects) >= 5:
                        break
        except ValueError:
            recommended_projects = []

    return render(request, 'user_profile.html', {'user_profile': user_profile, 'recommended_projects': recommended_projects})


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})


@login_required
def create_message(request, recipient_id):
    recipient = get_object_or_404(User, pk=recipient_id)
    sender = request.user

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            message.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('message_list')
    else:
        form = MessageForm()

    return render(request, 'message_form.html', {'form': form})


@login_required
def message_list(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    messages = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user)).order_by('-timestamp')
    return render(request, 'message_list.html', {'messages': messages, 'user_profile': user_profile})

class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'

class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'


#Since we want to make the data from APOD API as an object, we will create this class in order to send it as an object to the front end
class NasaAPOD:
    def __init__(self, title, url, explanation):
        self.title = title
        self.url = url
        self.explanation = explanation
 
#  We will do the same for the Mars Rover API
class MarsRoverPhoto:
    def __init__(self, photos):
        self.photos = photos



