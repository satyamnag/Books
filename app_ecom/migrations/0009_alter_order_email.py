# Generated by Django 5.1.2 on 2024-11-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ecom', '0008_alter_order_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=1000),
        ),
    ]
