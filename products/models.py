from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="وصف المنتج", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='products/', verbose_name="صورة المنتج", blank=True, null=True)

    def __str__(self):
        return self.name
    image = models.ImageField(upload_to='products/', blank=True, null=True)