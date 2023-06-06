from django.urls import path

from .views import MySiteView


app_name = 'mysite'

urlpatterns = [
    path('example/', MySiteView.as_view(), name='example')
]