import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

def avatar_upload_path(instance, filename):
    """Gera caminho único para o avatar do usuário."""
    ext = filename.split('.')[-1].lower()
    
    # Santiza o nome do arquivo para evitar problemas de segurança
    safe_username = ''.join(c for c in instance.user.username if c.isalnum() or c in (' ', '.', '_')).rstrip()
    
    filename = f"{safe_username}_avatar.{ext}"
    return os.path.join('avatars', filename)
    
class Profile(models.Model):
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(upload_to=avatar_upload_path, null=True, blank=True) 
    phone = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.username} - {self.role}"
