from django.urls import path
from . import views

urlpatterns = [

    # ================= HOME =================
    path('', views.home, name='home'),

    # ================= PRODUCTS =================
    path('products/', views.products_page, name='products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    # ================= CART =================
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),

    # ================= CHECKOUT =================
    path('checkout/', views.checkout, name='checkout'),
    path('order/success/', views.order_success, name='order_success'),

    # ================= AUTH =================
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ================= ORDERS =================
    path('orders/', views.orders_page, name='orders'),
    path('order/cancel/<int:id>/', views.cancel_order, name='cancel_order'),

]