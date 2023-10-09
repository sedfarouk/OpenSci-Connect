from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=256, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=128)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    required_skills = models.CharField(max_length=256)
    status = models.CharField(max_length=64, choices=[('active', 'Active'), ('completed', 'Completed'), ('in_progress', 'In Progress')])
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=128)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"From {self.sender} to {self.recipient} ({self.timestamp})"
    
    
class UserProjectInteraction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    interest_level = models.CharField(max_length=64, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], blank=True, null=True)
    contribution = models.TextField(blank=True, null=True)