from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from home_module.models import Public
from order_module.froms import OrderForm


class OrderCreateView(View):

    def get(self, request):
        form = OrderForm()
        information = Public.objects.filter(is_active=True).first()
        context = {
            'form': form,
            'information': information
        }
        return render(request, 'order_module/order_page.html', context)

    def post(self, request):
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({
                'success': True,
                'message': 'سفارش شما با موفقیت ثبت شد.'
            })
        return JsonResponse({
            'success': False,
            'errors': form.errors.get_json_data()
        }, status=400)