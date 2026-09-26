from django.shortcuts import render

# Create your views here.


def contact_me(request):
    return render(request, 'contact_module/contact_me.html')
