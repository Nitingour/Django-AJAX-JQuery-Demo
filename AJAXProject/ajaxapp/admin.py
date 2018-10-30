from django.contrib import admin
from ajaxapp.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['pname','price','description' ]


admin.site.register(Product,ProductAdmin)
