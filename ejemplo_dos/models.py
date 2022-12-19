from django.db import models
from django.contrib.auth.admin import User
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    publicado_el = models.DateField()
    image = models.ImageField(upload_to='posteos',null=True, blank=True)
    
class Avatar(models.Model): 
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='avatar')
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
    
