from django.shortcuts import render


def index_view(request):
    return render(request, 'landing/index.html')


def pricing_view(request):
    return render(request, 'landing/pricing.html')


def support_view(request):
    return render(request, 'landing/support.html')


def about_view(request):
    return render(request, 'landing/about.html')
