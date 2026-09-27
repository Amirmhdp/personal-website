from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'project_type',
            'description',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        ]

        widgets = {
            'project_type': forms.Select(attrs={
                'class': 'h-11 w-full appearance-none rounded-lg border border-border bg-background/70 px-4 text-sm text-muted outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/10',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full resize-none rounded-lg border border-border bg-background/70 px-4 py-3 text-sm leading-7 text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',
                'placeholder': 'لطفاً توضیحات کامل پروژه خود را بنویسید...',
                'rows': 5,
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'h-11 w-full rounded-lg border border-border bg-background/70 px-4 text-sm text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',
                'placeholder': 'نام خود را وارد کنید',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'h-11 w-full rounded-lg border border-border bg-background/70 px-4 text-sm text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',
                'placeholder': 'نام خانوادگی خود را وارد کنید',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'h-11 w-full rounded-lg border border-border bg-background/70 px-4 pl-11 text-sm text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',
                'placeholder': 'test@gmail.com',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'h-11 w-full rounded-lg border border-border bg-background/70 px-4 pl-11 text-sm text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',
                'placeholder': '۰۹۱۲۳۴۵۶۷۸۹',
            }),
        }
        labels = {
            'project_type': 'نوع پروژه',
            'description': 'توضیحات پروژه',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'شماره تلفن',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['project_type'].choices = [
            ('', 'نوع پروژه خود را انتخاب کنید'),
            *Order.PROJECT_TYPE_CHOICES,
        ]