# Generated by Django 5.1.2 on 2024-10-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ecom', '0002_rename_products_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=1000)),
                ('book_author', models.CharField(max_length=1000)),
                ('book_cover', models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT58P55blSKZmf2_LdBoU7jETl6OiB2sjYy9A&s')),
                ('book_rating', models.FloatField()),
                ('book_rating_count', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField()),
                ('mrp', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('product_description', models.TextField()),
                ('product_details', models.TextField()),
                ('about_the_author', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]