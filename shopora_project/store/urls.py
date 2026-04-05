from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase/<int:cart_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:cart_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.order_success, name='order_success'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('products/', views.products_page, name='products'),
    path('orders/', views.orders_page, name='orders'),
]