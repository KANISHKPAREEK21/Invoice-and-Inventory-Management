from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('',  auth_views.LoginView.as_view()),
    # path('', auth_views.LoginView.as_view(template_name='invoice/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='invoice/login.html'), name='login'),
    path('', login_required(views.home), name='home'), 

    path('create_product/', login_required(views.create_product), name='create_product'),
    path('view_product/', login_required(views.view_product), name='view_product'),
    path('edit_product/<int:pk>', login_required(views.edit_product), name='edit_product'),
    path('delete_product/<int:pk>/', login_required(views.delete_product), name='delete_product'),
    # path('upload_product_excel', views.upload_product_from_excel, name='upload_product_excel'),
    path('product_price/<int:pk>/', views.product_price, name='product_price'),

    #start  customer
    path('create_customer/', login_required(views.create_customer), name='create_customer'),
    path('view_customer/', login_required(views.view_customer), name='view_customer'),
    path('edit_customer/<int:pk>', login_required(views.edit_customer), name='edit_customer'),
    path('delete_customer/<int:pk>/', login_required(views.delete_customer), name='delete_customer'),
    path('customer_contact/<int:pk>/', views.customer_contact, name='customer_contact'),
    path('customer_invoice_download/<int:pk>/', views.customer_invoice_download, name='customer_contact'),

    # end  for customer

    path('create_invoice/', login_required(views.create_invoice), name='create_invoice'),
    path('view_invoice/', login_required(views.view_invoice), name='view_invoice'),
    path('delete_invoice/<int:pk>/', login_required(views.delete_invoice), name='delete_invoice'),
    # path('delete_all_invoice/', login_required(views.delete_all_invoice), name='delete_all_invoice'),
    path('download_all_invoice/', login_required(views.download_all), name='download_all_invoice'),
    path('view_invoice_detail/<int:pk>/', login_required(views.view_invoice_detail), name='view_invoice_detail'),
    path('download_invoice_detail/<int:pk>/', login_required(views.download_invoice_detail), name='download_invoice_detail'),
    
    path('add_expense/', login_required(views.add_expense), name='add_expense'),
    path('view_expense/', login_required(views.view_expense), name='view_expense'),
    path('delete_expense/<int:pk>/', login_required(views.delete_expense), name='delete_expense'),

]
