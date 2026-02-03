from django.shortcuts import render
from django.contrib import messages
   
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print("NAME:", name)
        print("EMAIL:", email)
        print("MESSAGE:", message)
        
        # Django popup message
        messages.success(request, "✅ Message sent successfully!")

    return render(request, "websites/index.html")


# def home(request):
#     return render(request, 'websites/index.html')