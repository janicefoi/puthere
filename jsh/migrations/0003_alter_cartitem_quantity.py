# Generated by Django 4.2.6 on 2023-11-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsh', '0002_cart_cartitem_remove_orderitem_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
