from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField(default=0)
    product_unit = models.CharField(max_length=255)
    product_is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product_name)

        # this is commented
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_contact = models.CharField(max_length=255)
    customer_amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer_name)
        # this is commented


class Invoice(models.Model):
    date = models.DateField(auto_now_add=True)
    customer = models.TextField(default='')
    contact = models.CharField(
        max_length=255, default='', blank=True, null=True)
    comments = models.TextField(default='', blank=True, null=True)
    total = models.FloatField(default=0)
    # YES = 'Yes'
    # NO = 'No'
    # CHOICES = (
    #     (NO, 'NO'),
    #     (YES, 'YES'),
    # )
    # gst = models.CharField(max_length=3, choices=CHOICES)

    def __str__(self):
        return str(self.id)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=1)

    @property
    def get_total_bill(self):
        total = float(self.price) * float(self.amount)
        return total
