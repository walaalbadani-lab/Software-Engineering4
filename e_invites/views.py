from django.shortcuts import render
from django.utils import timezone


def home(request):
    # متغيرات محلية وشروط وحلقات
    site_name = "Electronic Invitations"
    arabic_name = "دعوات إلكترونية"
    current_date = timezone.now()
    service_available = True
    customer_name = ""
    categories = ["دعوات", "رسومات", "ورقيات", "فيديوهات"]

    products_data = [
        ("رسم رقمي", "e_invites/10.jpg", 1000, "image"),
        ("بشارة مواليد", "e_invites/11.jpg", 1000, "image"),
        ("حسب الطلب", "e_invites/13.jpg", 1000, "image"),
        ("دعوة عرس", "e_invites/19.jpg", 1000, "image"),
        ("عيد أضحى", "e_invites/14.jpg", 1000, "image"),
        ("جرائد وورقيات", "e_invites/18.jpg", 500, "image"),
        ("فيديو دعوة إلكترونية", "e_invites/20.mp4", 3000, "video"),
    ]

    products = []

    for index, product in enumerate(products_data, start=1):
        products.append(
            {
                "number": index,
                "name": product[0],
                "file": product[1],
                "price": product[2],
                "type": product[3],
                "featured": index <= 3,
            }
        )

    products_count = len(products)

    if service_available:
        service_message = "نستقبل طلباتكم حالياً"
    else:
        service_message = "الخدمة متوقفة مؤقتاً"

    if products_count >= 7:
        collection_status = "مجموعة متنوعة من الخدمات"
    elif products_count >= 4:
        collection_status = "مجموعة متوسطة"
    else:
        collection_status = "مجموعة محدودة"

    if service_available:
        if products_count > 0:
            order_status = "يمكنك إرسال طلبك الآن"
        else:
            order_status = "لا توجد خدمات متاحة"
    else:
        order_status = "الطلبات متوقفة مؤقتاً"

    reviews_data = [
        ("سارة محمد", "التصميم جميل والتنفيذ كان سريعاً."),
        ("ريم أحمد", "أعجبني التعامل وجودة الدعوة."),
        ("هدى علي", "خدمة ممتازة ونتيجة رائعة."),
    ]

    reviews = []

    review_index = 0

    while review_index < len(reviews_data):
        reviews.append(
            {
                "name": reviews_data[review_index][0],
                "message": reviews_data[review_index][1],
            }
        )

        review_index += 1

    context = {
        "site_name": site_name,
        "arabic_name": arabic_name,
        "current_date": current_date,
        "service_available": service_available,
        "service_message": service_message,
        "customer_name": customer_name,
        "categories": categories,
        "products": products,
        "products_count": products_count,
        "collection_status": collection_status,
        "order_status": order_status,
        "reviews": reviews,
    }

    return render(request, "e_invites/home.html", context)


def about(request):
    # متغيرات محلية وشروط وحلقات
    site_name = "Electronic Invitations"
    arabic_name = "دعوات إلكترونية"
    current_date = timezone.now()
    version = 2
    team_members = ["ولاء"]
    values_names = ["الجودة", "الإبداع", "السرعة"]

    if version == 1:
        version_status = "الإصدار الأول"
    elif version == 2:
        version_status = "الإصدار المطور"
    else:
        version_status = "الإصدار الحديث"

    values = []

    for index, value_name in enumerate(values_names, start=1):
        values.append(
            {
                "number": index,
                "name": value_name,
            }
        )

    context = {
        "site_name": site_name,
        "arabic_name": arabic_name,
        "current_date": current_date,
        "version": version,
        "version_status": version_status,
        "team_members": team_members,
        "values": values,
    }

    return render(request, "e_invites/about.html", context)


def order(request):
    # متغيرات محلية وشروط وحلقات
    site_name = "Electronic Invitations"
    arabic_name = "دعوات إلكترونية"
    current_date = timezone.now()
    sent = False
    customer_name = ""
    selected_service = ""
    selected_price = 0

    services = [{"name": "رسم رقمي", "price": 1000},
        {"name": "بشارة مواليد", "price": 1000},
        {"name": "حسب الطلب", "price": 1000},
        {"name": "دعوة عرس", "price": 1000},
        {"name": "عيد أضحى", "price": 1000},
        {"name": "جرائد وورقيات", "price": 500},
        {"name": "فيديو دعوة إلكترونية", "price": 3000},
    ]

    if request.method == "POST":
        customer_name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        selected_service = request.POST.get("service", "").strip()
        request_details = request.POST.get("details", "").strip()

        if customer_name and email and password and selected_service and request_details:
            for service in services:
                if service["name"] == selected_service:
                    selected_price = service["price"]
                    break

            sent = True
        else:
            sent = False

    context = {
        "site_name": site_name,
        "arabic_name": arabic_name,
        "current_date": current_date,
        "services": services,
        "sent": sent,
        "customer_name": customer_name,
        "selected_service": selected_service,
        "selected_price": selected_price,
    }

    return render(request, "e_invites/order.html", context)