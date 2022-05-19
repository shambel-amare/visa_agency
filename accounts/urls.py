from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('customer_register/', views.customer_register.as_view(),
         name='customer_register'),
    path('employee_register/', views.agent_register.as_view(),
         name='agent_register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/password-reset/',
         auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('user/password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/password-reset-sent/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('user/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
