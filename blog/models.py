from django.conf import settings #import to pull from other files
from django.db import models
from django.utils import timezone
#class defines the object
#post is the model name (classes must be started with uppercase)
#models.Model defines post as a Django model with .Model as the method
#ForeignKey links a model to another model (points data at another table)
#Charfield  defines text with a limited amount of characters
#DateTimeField is just daete and time
#Textfield is unlimited text
#use makemigrations and migrate blog to use django to add the model to the database (SQLite to store data)
class Post(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self): 
        self.published_date = timezone.now()
        self.save()

        def __str__(self):
            return self.title
