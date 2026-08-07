from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=100, verbose_name="اسم المستخدم")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    password = models.CharField(max_length=100, verbose_name="كلمة المرور")

    def __str__(self):
        return self.username