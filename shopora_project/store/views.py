from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Cart, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ================= HOME =================
def home(request):
    categories = Category.objects.all()
    data = []

    for category in categories:
        products = Product.objects.filter(category=category)
        data.append({
            'category': category,
            'products': products
        })

    return render(request, 'store/home.html', {'data': data})


# ================= PRODUCT DETAIL =================
@login_required
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_details.html', {'product': product})


# ================= ADD TO CART =================
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


# ================= CART VIEW =================
@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:
        item.total = item.product.price * item.quantity

    total_price = sum(item.total for item in cart_items)

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


# ================= REMOVE FROM CART =================
@login_required
def remove_from_cart(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)
    item.delete()
    return redirect('cart')


# ================= INCREASE QUANTITY =================
@login_required
def increase_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')


# ================= DECREASE QUANTITY =================
@login_required
def decrease_quantity(request, cart_id):
    item = get_object_or_404(Cart, id=cart_id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


# ================= CHECKOUT =================
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Create Order
        order = Order.objects.create(
            user=request.user,
            name=name,
            address=address,
            phone=phone,
            total_price=total_price
        )

        # Create Order Items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Clear cart
        cart_items.delete()

        return redirect('order_success')

    return render(request, 'store/checkout.html', {
        'total_price': total_price
    })


# ================= ORDER SUCCESS =================
@login_required
def order_success(request):
    return render(request, 'store/success.html')


# ================= REGISTER =================
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists ❌")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created successfully ✅")
        return redirect('login')

    return render(request, 'store/register.html')


# ================= LOGIN =================
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials ❌")

    return render(request, 'store/login.html')


# ================= LOGOUT =================
def user_logout(request):
    logout(request)
    return redirect('login')


# ================= PRODUCTS PAGE =================
def products_page(request):
    products = Product.objects.all()

    query = request.GET.get('q')
    sort = request.GET.get('sort')

    if query:
        products = products.filter(name__icontains=query)

    if sort == "low":
        products = products.order_by('price')
    elif sort == "high":
        products = products.order_by('-price')

    return render(request, 'store/products.html', {'products': products})
    


# ================= ORDERS PAGE =================
@login_required
def orders_page(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/orders.html', {'orders': orders})


# ================= CANCEL ORDER =================
@login_required
def cancel_order(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    order.status = "Cancelled"
    order.save()
    return redirect('orders')