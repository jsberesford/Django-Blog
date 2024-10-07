from django.contrib import admin 
from .models import Post #imports the defined model

admin.site.register(Post) #register the model to the admin page
# Register your models here.
