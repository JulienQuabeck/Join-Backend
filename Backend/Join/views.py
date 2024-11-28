from django.shortcuts import render
from .models import contact
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializer import ContactSerializer


# Create your views here.

class contactModelViewSet(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = ContactSerializer
