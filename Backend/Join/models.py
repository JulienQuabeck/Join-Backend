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

    def __str__(self):
        return self.Name

class task(models.Model):
    # muss noch angepasst / überarbeitet werden
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    contacts = models.ForeignKey(contact, on_delete=models.CASCADE)
    date = models.DateField(max_length=50)
    priority = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    subtasks = models.JSONField()
    subtasksProgress = models.IntegerField()
    colum = models.CharField(max_length=50)