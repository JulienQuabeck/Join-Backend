from django.shortcuts import render
from models import contact

# Create your views here.
class ModelListView(ListView):
    model = contact
    template_name = "./Join/Frontend/html/contacts.html"
