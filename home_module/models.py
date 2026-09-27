from django.db import models

# Create your models here.


class Public(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام سایت')
    domain = models.URLField(max_length=200, verbose_name='دامنه سایت')
    developer_name = models.CharField(max_length=100, verbose_name='نام سازنده')
    about_developer = models.TextField(verbose_name='درباره سازنده')
    short_description_developer = models.TextField(null=True, blank=True, verbose_name='توضیح کوتاه')
    github_url = models.URLField(max_length=200, blank=True, verbose_name='آدرس گیت‌هاب')
    instagram_url = models.URLField(max_length=200, blank=True, verbose_name='آدرس اینستاگرام')
    email = models.EmailField(max_length=254, verbose_name='ایمیل')
    phone_number = models.CharField(max_length=20, verbose_name='شماره تلفن')
    completed_projects = models.PositiveIntegerField(default=0, verbose_name='تعداد پروژه‌های انجام شده')
    years_of_experience = models.PositiveIntegerField(default=0, verbose_name='سال تجربه')
    logo = models.FileField(upload_to='site/', blank=True, null=True, verbose_name='لوگوی سایت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    copy_right = models.CharField(max_length=200, null=True, blank=True, verbose_name='متن گپی رایت')

    class Meta:
        verbose_name = 'اطلاعات سایت'
        verbose_name_plural = 'اطلاعات سایت'

    def __str__(self):
        return self.site_name

class FooterLink(models.Model):
    LINK_TYPE_CHOICES = (
        ('quick', 'لینک سریع'),
        ('site', 'لینک سایت'),
    )

    title = models.CharField(
        max_length=100,
        verbose_name='عنوان لینک'
    )
    url = models.CharField(
        max_length=255,
        verbose_name='آدرس لینک'
    )
    link_type = models.CharField(
        max_length=20,
        choices=LINK_TYPE_CHOICES,
        verbose_name='نوع لینک'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال'
    )


    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک‌های فوتر'

    def __str__(self):
        return self.title
