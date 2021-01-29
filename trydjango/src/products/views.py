from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
from django.http import Http404

# Create your views here.
def product_details_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {
        "object": obj
    }
    return render(request,'product/product_details.html', context )

def product_create_view(request, *args, **kwargs):
    initial_data = {
        "title": "Initial Title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request,'product/product_create.html', context )


def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
   
    context = {
        "object": obj
    }
    return render(request, 'product/details.html', context)

def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id = my_id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../../")
    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)

def product_list_view(request, *args, **kwargs):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product/product_list.html", context)


# def product_create_view(request, *args, **kwargs):
#     if request.method == 'POST':
#         my_title = request.POST.get('title')
#         print(my_title)
#     context = {}
#     return render(request,'product/product_create.html', context )

# def product_create_view(request, *args, **kwargs):
#     my_form = ProductForm()
#     if request.method == 'POST':
#         my_form = ProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request,'product/product_create.html', context )