from django.urls import path
from . import views

urlpatterns = [
  path('', views.userDashboard, name='userDashboard'),
  path('register/', views.register, name='register'),
  path('login/', views.userLogin, name='userLogin'),
  path('otpLogin/', views.otpLogin, name='otpLogin'),
  path('otpVerification/', views.otpVerification, name='otpVerification'),
  path('userLogout/', views.userLogout, name='userLogout'),
  
  path('userDashboard/', views.userDashboard, name='userDashboard'),
  path('myOrders/', views.myOrders, name='myOrders'),
  path('orderDetails/<int:order_id>/', views.orderDetails, name='orderDetails'),
  path('editProfile/', views.editProfile, name='editProfile'),
  path('myAddress/', views.myAddress, name='myAddress'),
  path('add_address/', views.add_address, name='add_address'),
  path('edit_address/<int:id>/', views.edit_address, name='edit_address'),
  path('delete_address/<int:id>/', views.delete_address, name='delete_address'),
]