from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home_module/home.html')

def header_partial(request):
    return render(request, 'shared/header.html')

def footer_partial(request):
    return render(request, 'shared/footer.html')
