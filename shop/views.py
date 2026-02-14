from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request , 'shop/shop.html')

def product_detail(request):
    return render(request, 'shop/single-product-details.html')