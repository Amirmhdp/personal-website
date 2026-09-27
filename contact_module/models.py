from django.db import models

# Create your models here.

class ContactMessage(models.Model):

    SUBJECT_CHOICES = (
        ('website_design', 'سفارش طراحی سایت'),
        ('project_development', 'توسعه پروژه'),
        ('consultation', 'مشاوره'),
        ('other', 'سایر موارد'),
    )

    first_name = models.CharField(max_length=100, verbose_name='نام')

    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')

    phone_number = models.CharField(max_length=20, verbose_name='شماره تماس')

    subject = models.CharField(max_length=30, choices=SUBJECT_CHOICES,verbose_name='موضوع')

    message = models.TextField(verbose_name='پیام')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.get_subject_display()}'