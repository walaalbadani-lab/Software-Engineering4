from django.shortcuts import render, redirect
from products.models import Product
from account.models import UserAccount
from django.contrib import messages

def home(request):
    products = Product.objects.all()

    if request.method == "POST":
        action = request.POST.get("action")

        # تسجيل حساب جديد
        if action == "register":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if UserAccount.objects.filter(email=email).exists():
                messages.error(request, "البريد الإلكتروني مستخدم مسبقاً")
            else:
                UserAccount.objects.create(username=username, email=email, password=password)
                messages.success(request, "تم إنشاء الحساب بنجاح")

        # تسجيل الدخول
        elif action == "login":
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = UserAccount.objects.filter(email=email, password=password).first()
            if user:
                messages.success(request, f"مرحباً {user.username}")
            else:
                messages.error(request, "بيانات الدخول غير صحيحة")

        # إرسال طلب
        elif action == "order":
            service = request.POST.get("service")
            details = request.POST.get("details")
            messages.success(request, f"تم استلام طلبك ({service}) بنجاح. سيتم التواصل معك قريباً.")

    context = {
        "products": products,
    }
    return render(request, "e_invites/home.html", context)