from django.db.models import Q
from products.models import Product


def search_designs(query):
    """
    يبحث عن التصاميم من قاعدة البيانات
    باستخدام اسم التصميم أو وصفه.
    """

    if not query:
        return Product.objects.none()

    results = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    ).distinct()

    return results