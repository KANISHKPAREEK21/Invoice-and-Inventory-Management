# Generated by Django 4.2.13 on 2024-05-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_remove_invoicedetail_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
