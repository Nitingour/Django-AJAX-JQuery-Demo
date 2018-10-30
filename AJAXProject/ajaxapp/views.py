from django.shortcuts import render
from ajaxapp.forms import ProductForm
from django.contrib import messages
from django.http import JsonResponse
from ajaxapp.models import Product
# Create your views here.
def addproduct(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Product Added Successfully...')
            form=ProductForm()
            return render(request,"ajaxapp/product.htm",{'form':form})
    else:
        form=ProductForm()
        #print(form)
        return render(request,"ajaxapp/product.htm",{'form':form})


def checkProduct(request):
     product = request.GET.get('pname', None)
     print("PRODUCT IN VIEW>>>>>>>>",product)
     data = {
        'is_taken': Product.objects.filter(pname__iexact=product).exists()
        }
     print(data)
     return JsonResponse(data)
