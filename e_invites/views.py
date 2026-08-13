from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.dateparse import parse_date

from .models import Order
from products.models import Product


PRICES = {
    "رسم رقمي": 1000,
    "مواليد": 1000,
    "زفاف": 1000,
    "تخرج": 1000,
    "فيديو": 300,
    "جرائد وورقيات": 500,
}


def home(request):
    notes = list(Order.objects.all()[:8])

    return render(request, "e_invites/home.html", {
        "products": Product.objects.all(),
        "q": (request.GET.get("q") or "").strip(),
        "notifications": notes,
        "notification_count": Order.objects.count(),
    })


def about(request):
    return render(request, "e_invites/about.html")


def product_list(request):
    return redirect("home")


def order(request):
    selected = (
        request.POST.get("occasion")
        or request.GET.get("product")
        or ""
    ).strip()

    if request.method == "POST":
        price = PRICES.get(selected)

        if price is None:
            product = Product.objects.filter(title=selected).first()
            if product is None:
                product = Product.objects.filter(name=selected).first()
            price = int(getattr(product, "price", 0) or 0) if product else None

        event_date = parse_date(request.POST.get("date") or "")
        phone = request.POST.get("phone", "").strip()
        place = request.POST.get("place", "").strip()

        if not selected or price is None:
            messages.error(request, "اختر نوع الدعوة.")
        elif not event_date:
            messages.error(request, "أدخل التاريخ.")
        elif not phone or not place:
            messages.error(request, "أكمل المكان ورقم التواصل.")
        else:
            Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                occasion=selected,
                price=price,
                date=event_date,
                phone=phone,
                place=place,
                names=request.POST.get("names", "").strip(),
                message=request.POST.get("message", "").strip(),
            )
            messages.success(request, "تم تسجيل الطلب.")
            return redirect("home")

    return render(request, "e_invites/order.html", {
        "selected_product": selected,
    })