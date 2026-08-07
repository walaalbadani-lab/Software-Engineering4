from django.shortcuts import render, redirect
from .models import UserAccount

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        UserAccount.objects.create(
            username=username,
            email=email,
            password=password
        )
        return redirect("account:login")

    return render(request, "account/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = UserAccount.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            return redirect("e_invites:home")

        return render(request, "account/login.html", {
            "error": "بيانات الدخول غير صحيحة"
        })

    return render(request, "account/login.html")