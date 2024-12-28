from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import *

cart={}

# Create your views here.
class BookListView(ListView):
    model=Book
    template_name='app_ecom/index.html'
    context_object_name='books'
    paginate_by=8

    def get_queryset(self):
        queryset = super().get_queryset()
        book_name = self.request.GET.get('book_name')
        if book_name:
            queryset = queryset.filter(book_name__icontains=book_name)
        return queryset

class BookDetailView(DetailView):
    model=Book
    template_name='app_ecom/details.html'


def checkout(request):
    if request.method=='POST':
        items=request.POST.get('items', '')
        email=request.POST.get('email', '')
        first_name=request.POST.get('first_name', '')
        last_name=request.POST.get('last_name', '')
        address1=request.POST.get('address1', '')
        address2=request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        pincode=request.POST.get('pincode', '')
        total=request.POST.get('total', '')
        order=Order(items=items,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    address1=address1,
                    address2=address2,
                    city=city,
                    state=state,
                    pincode=pincode,
                    total=total)
        order.save()
    return render(request, "app_ecom/checkout.html")