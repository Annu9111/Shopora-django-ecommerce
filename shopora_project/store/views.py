from django.shortcuts import render
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    data = []

    for category in categories:
        products = Product.objects.filter(category=category)[:3]
        data.append({
            'category': category,
            'products': products
        })

    return render(request, 'store/home.html', {'data': data})