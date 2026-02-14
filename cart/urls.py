from django.urls import path
from cart.views import checkout
app_name = 'cart'
urlpatterns = [
    path('checkout' , checkout , name = 'index'),

]
