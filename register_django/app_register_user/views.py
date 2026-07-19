from django.shortcuts import render
from .models import Users


def home(request):
    return render(request, "users/home.html")


def users(request):
    new_user = Users()
    new_user.name = request.POST.get("name")
    new_user.age = request.POST.get("age")
    new_user.save()

    users = {"users": Users.objects.all()}

    return render(request, "users/users.html", users)
