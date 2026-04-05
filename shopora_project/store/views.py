from django.shortcuts import render
from .models import Product, Category,Cart,Order
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product_details.html', {'product': product})



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def cart_view(request):
    cart_items = Cart.objects.all()

    for item in cart_items:
        item.total = item.product.price * item.quantity

    total_price = sum(item.total for item in cart_items)

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })
    
@login_required
def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    item.delete()
    return redirect('cart')


def increase_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)
    item.quantity += 1
    item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def decrease_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()  # if quantity becomes 0 → remove item

    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def checkout(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        Order.objects.create(
            name=name,
            address=address,
            phone=phone,
            total_price=total_price
        )

        cart_items.delete()  # clear cart after order

        return redirect('order_success')    

    return render(request, 'store/checkout.html', {
        'total_price': total_price
    })
    
def order_success(request):
    return render(request, 'store/success.html')    




def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ✅ CHECK IF USER EXISTS
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists ❌")
            return redirect('register')

        # ✅ CREATE USER
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created successfully ✅")
        return redirect('login')

    return render(request, 'store/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

            