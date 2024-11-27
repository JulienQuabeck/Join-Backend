from django.db import models

# nach Änderungen ausführen (in der env!!):
# py manage.py makemigrations
# py manage.py migrate 

# Create your models here.
class contact(models.Model):
    Name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    color = models.CharField(max_length=10)

class task(models.Model):
    # muss noch angepasst / überarbeitet werden
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    priority = models.CharField(max_length=10)
    subtasks = models.CharField(max_length=50)
    subtasksProgress = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    colum = models.CharField(max_length=50)
    contacts = models.CharField(max_length=50)
    token = models.CharField(max_length=50)