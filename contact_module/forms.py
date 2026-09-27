from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'subject',
            'message',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class':  'h-11 w-full rounded-lg border border-border  bg-background/70 px-8.75 text-sm text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',

                'placeholder': 'نام خود را وارد کنید',
            }),

            'last_name': forms.TextInput(attrs={
                'class':  'h-11 w-full rounded-lg border border-border bg-background/70 px-8.75 text-sm text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',

                'placeholder': 'نام خانوادگی خود را وارد کنید',
            }),

            'phone_number': forms.TextInput(attrs={
                'class':  'h-11 w-full rounded-lg border border-border bg-background/70 px-8.75 text-sm text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',

                'placeholder': '۰۹۱۲۳۴۵۶۷۸۹',
            }),

            'subject': forms.Select(attrs={
                'class':  'h-11 w-full appearance-none rounded-lg border border-border bg-background/70 px-8.75 text-sm text-muted outline-none transition focus:border-primary focus:ring-2 focus:ring-primary/10',

            }),

            'message': forms.Textarea(attrs={
                'class':  'w-full resize-none rounded-lg border border-border bg-background/70 px-8.75 py-3 text-sm leading-7 text-text outline-none transition placeholder:text-muted/50 focus:border-primary focus:ring-2 focus:ring-primary/10',
                'placeholder': 'پیام خود را برای ما بنویسید...',
                'rows': 5,
            }),
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تماس',
            'subject': 'موضوع',
            'message': 'پیام شما',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['subject'].choices = [
            ('', 'موضوع خود را انتخاب کنید'),
            *ContactMessage.SUBJECT_CHOICES,
        ]