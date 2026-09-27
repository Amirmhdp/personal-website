from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from home_module.models import Public
from .forms import ContactMessageForm


class ContactCreateView(View):

    def get(self, request):
        form = ContactMessageForm()
        information = Public.objects.filter(is_active=True).first()

        context = {
            'form': form,
            'information': information
        }

        return render(request,'contact_module/contact_me.html',context)

    def post(self, request):
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({
                'success': True,
                'message': 'پیام شما با موفقیت ارسال شد.'
            })

        return JsonResponse({
            'success': False,
            'errors': form.errors.get_json_data()
        }, status=400)
