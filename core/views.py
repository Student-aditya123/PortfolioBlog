# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Message sent successfully!")
        return redirect("home")

    return render(request, "websites/index.html")
