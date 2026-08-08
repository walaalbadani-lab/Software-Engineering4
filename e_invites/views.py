from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from products.models import Product
from account.models import UserAccount

def home(request):
    search_query = request.GET.get('search', '').strip()
    message = None
    message_type = None

    if request.method == "POST":
        action = request.POST.get('action')

        # تسجيل حساب جديد
        if action == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                message = "اسم المستخدم موجود مسبقاً"
                message_type = "error"
            elif User.objects.filter(email=email).exists():
                message = "البريد الإلكتروني مستخدم من قبل"
                message_type = "error"
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                UserAccount.objects.create(user=user)   # حفظ في قاعدة البيانات
                message = "تم التسجيل بنجاح! يمكنك تسجيل الدخول الآن"
                message_type = "success"

        # تسجيل الدخول
        elif action == 'login':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
                if user:
                    login(request, user)
                    message = f"مرحباً {user.username} ✓"
                    message_type = "success"
                    return redirect('home')
                else:
                    message = "كلمة المرور خاطئة"
                    message_type = "error"
            except:
                message = "البريد غير مسجل"
                message_type = "error"

        # خروج
        elif action == 'logout':
            logout(request)
            return redirect('home')

    # البحث
    products = Product.objects.all().order_by('-id')
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    static_products = [
        {"name": "رسم رقمي", "price": "1000", "img": "e_invites/10.jpg"},
        {"name": "بشارة مواليد", "price": "1000", "img": "e_invites/11.jpg"},
        {"name": "حسب الطلب", "price": "1000", "img": "e_invites/13.jpg"},
        {"name": "عيد", "price": "1000", "img": "e_invites/14.jpg"},
        {"name": "حفل زفاف", "price": "1000", "img": "e_invites/19.jpg"},
        {"name": "الشعار", "price": "1000", "img": "e_invites/22.jpg"},
    ]

    if search_query:
        q = search_query.lower()
        static_products = [item for item in static_products if q in item["name"].lower()]

    context = {
        'products': products,
        'static_products': static_products,
        'search_query': search_query,
        'total_count': len(static_products) + products.count(),
        'message': message,
        'message_type': message_type,
    }
    return render(request, 'e_invites/home.html', context)