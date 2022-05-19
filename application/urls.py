from django.urls import path
from .views import *


urlpatterns = [
    path('main/', dashboard, name='dashboard'),
    path('main/start_application/',
         start_application, name='main_application'),
    path('main/application/search-result',
         search_application, name='search_application'),
    path('main/application/edit/<application_id>',
         edit_application, name='edit_application'),
    path('main/application/see/<application_id>',
         see_application, name='see_application'),
    path('main/admin/approval/',
         admin_approval, name='admin_approval'),

]
