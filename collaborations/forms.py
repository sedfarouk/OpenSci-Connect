from django import forms
from .models import Project, Message, UserProfile


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'required_skills'] 
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'content']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  
        fields = ['skills', 'interests']
