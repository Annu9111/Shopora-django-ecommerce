from django.shortcuts import render
from .models import Product, Category,Cart
from django.shortcuts import render, redirect ,get_object_or_404

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

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product_details.html', {'product': product})




def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER'))


def cart_view(request):
    cart_items = Cart.objects.all()

    for item in cart_items:
        item.total = item.product.price * item.quantity

    total_price = sum(item.total for item in cart_items)

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    item.delete()
    return redirect('cart')

