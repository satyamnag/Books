from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=1000)
    book_author=models.CharField(max_length=1000)
    book_cover=models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT58P55blSKZmf2_LdBoU7jETl6OiB2sjYy9A&s')
    book_rating=models.FloatField()
    book_rating_count=models.PositiveIntegerField()
    selling_price=models.PositiveIntegerField()
    mrp=models.PositiveIntegerField()
    discount=models.PositiveIntegerField()
    about_the_author=models.TextField()

    def __str__(self):
        return self.book_name
    
class Order(models.Model):
    items=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    first_name=models.CharField(max_length=1000)
    last_name=models.CharField(max_length=1000)
    address1=models.CharField(max_length=1000)
    address2=models.CharField(max_length=1000)
    city=models.CharField(max_length=1000)
    state=models.CharField(max_length=1000)
    pincode=models.CharField(max_length=1000)
    total=models.CharField(max_length=200, default=0)