from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from tryout.forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.


def homepage_view(request, *args, **kwargs):
    print(request)
    # return HttpResponse("<h1> Hello World </h1>")  # string of html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Contact World </h1>")  # string of html code
    my_contact = {
        "my_number": 123,
        "my_email": "abc@xyz.com",
        "list": [2, 4, 6, 8]
    }
    return render(request, "contact.html", my_contact)


def product_detail_view(request):
    # obj = get_object_or_404(Product, id=1)
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     my_form = RawProductForm(request.POST)
#     context = {"form": my_form}
#     return render(request, "products/product_create.html", context)
