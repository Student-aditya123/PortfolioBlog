from django.shortcuts import render
from .models import Project
from .forms import ContactForm

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
