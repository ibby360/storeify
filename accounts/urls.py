from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('my_orders/', views.orders, name='orders'),
    path('order_detail/', views.order_detils, name='order_detail'),
    path('forgot_pasword', views.forgot_password, name='forgot_password')

]
