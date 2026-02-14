from django.urls import path
from shop.views import product , product_detail

app_name = 'shop'
urlpatterns = [
    path('' , product , name = 'index'),
    path('detail/', product_detail ,name = 'contact'),


]
