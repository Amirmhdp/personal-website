from django.db import models

# Create your models here.

class Order(models.Model):
    PROJECT_TYPE_CHOICES = (
        ('corporate', 'وب‌سایت شرکتی'),
        ('store', 'فروشگاه اینترنتی'),
        ('personal', 'وب‌سایت شخصی'),
        ('portfolio', 'وب‌سایت نمونه‌کار'),
        ('blog', 'وب‌سایت وبلاگی'),
        ('landing', 'لندینگ پیج'),
        ('educational', 'وب‌سایت آموزشی'),
        ('booking', 'سیستم رزرو و نوبت‌دهی'),
        ('dashboard', 'پنل مدیریت'),
        ('web_app', 'اپلیکیشن تحت وب'),
        ('custom', 'پروژه اختصاصی'),
        ('other', 'سایر'),
    )

    project_type = models.CharField(max_length=30, choices=PROJECT_TYPE_CHOICES, verbose_name='نوع پروژه')

    description = models.TextField(verbose_name='توضیحات پروژه')

    first_name = models.CharField(max_length=100, verbose_name='نام')

    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')

    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='ایمیل')

    phone_number = models.CharField(max_length=20, verbose_name='شماره تلفن')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت سفارش')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.get_project_type_display()}'
