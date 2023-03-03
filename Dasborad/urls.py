from django.urls import path
from . import views


urlpatterns = [
    path('dasboard/', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
    path('order/', views.order, name='order'),
    path('product/', views.product, name='product'),
]
