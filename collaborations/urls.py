from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', user_profile, name='user_profile'),
    path('create_project/', create_project, name='create_project'),
    path('create_message/<int:recipient_id>/', create_message, name='create_message'),
    path('message_list/', message_list, name='message_list'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('project_list/', ProjectListView.as_view(), name='project_list'),
    path('project_detail/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]
