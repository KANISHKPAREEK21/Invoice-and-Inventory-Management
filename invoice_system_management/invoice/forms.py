from django import forms
from django.forms import formset_factory

import datetime
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            # 'product_unit',
        ]
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_name',
                'placeholder': 'Enter name of the product',
            }),
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'product_price',
                'placeholder': 'Enter price of the product',
                'type': 'number',
            }),
            # 'product_unit': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'product_unit',
            #     'placeholder': 'Enter unit of the product',
            # }),
        }


        # this is commented
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'customer_name',
            'customer_contact',
            'customer_amount',
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_name',
                'placeholder': 'Enter name of the customer',
            }),
        }
        # this is commented


class InvoiceForm(forms.ModelForm):
    class Meta:

        model = Invoice
        fields = [
            'customer',
            'comments',
            'contact',
            'gst',
            # 'price'
            # 'email',
        ]
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control customer-dropdown',
                'id': 'invoice_customer',
                'placeholder': 'Enter name of the customer',
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_contact',
                'placeholder': 'Enter contact of the customer',
                'readonly':'readonly',
            }),
            # 'email': forms.EmailInput(attrs={
            #     'class': 'form-control',
            #     'id': 'invoice_email',
            #     'placeholder': 'Enter email of the customer',
            # }),
            'comments': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_comments',
                'placeholder': 'Enter comments',
            }),
            'gst': forms.CheckboxInput(attrs={
                'class' : 'form-check',
                'id': 'invoice_gst',
                'style':'width: 100%;'
            }),
            # 'price': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'invoice_detail_price',
            #     'placeholder': f'{Product.product_price}',
            # }),
        }
    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.filter(customer_is_delete=0)


class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = [
            'product',
            'amount',
            'price'
        ]
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control product-dropdown',
                'id': 'invoice_detail_product',
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_amount',
                'placeholder': '1',
                'type': 'number',
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_form-0-price',
                # 'placeholder': f'{Product.product_price}',
            }),
        }
    def __init__(self, *args, **kwargs):
        super(InvoiceDetailForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(product_is_delete=0)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'expense_name',
            'expense_cost'
        ]
        widgets = {
            'expense_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'expense_name',
                'placeholder': 'Enter Expense',
                
            }),
            'expense_cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'expense_cost',
                'placeholder': 'Enter price of the product',
                'type': 'number',
            }),
        }
        expense = models.CharField(max_length=255)
        cost = models.FloatField(max_length=255)
        is_active = models.BooleanField(default=True)


# class excelUploadForm(forms.Form):
#     file = forms.FileField()


InvoiceDetailFormSet = formset_factory(InvoiceDetailForm, extra=1)

ProductFormSet = formset_factory(ProductForm, extra=1)
