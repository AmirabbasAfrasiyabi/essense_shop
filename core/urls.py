from django.urls import path
from core.views import home , contact ,about

app_name = 'core'
urlpatterns = [
    path('' , home , name = 'index'),
    path('contact/', contact ,name = 'contact'),
    path('about/' , about , name = 'about'),

]
