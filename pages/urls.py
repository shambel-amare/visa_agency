from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('customer/howto_register/', views.howto, name='howto'),

]
