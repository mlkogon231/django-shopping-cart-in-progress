from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('store/<int:pk>', views.product_list, name='product_list_by_category'),
    path('store/<slug:title>',views.product_list, name='product_list_by_category'),
    path('store/<int:pk>/<slug:title>', views.product_detail, name='product_detail'),

]

