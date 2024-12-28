from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header='Book Store'
admin.site.site_title='Book Store'
admin.site.index_title='Manage Book Store'

class BookAdmin(admin.ModelAdmin):

    def soldout(self, request, queryset):
        queryset.update(selling_price="soldout", mrp="soldout", discount='soldout')

    soldout.short_description="Sold Out"
    list_display=('book_name', 'book_author', 'book_rating', 'book_rating_count', 'selling_price', 'mrp', 'discount')
    search_fields=('book_name',)
    actions=('soldout',)

admin.site.register(Book, BookAdmin)
admin.site.register(Order)