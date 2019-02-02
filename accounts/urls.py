from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('', include('django.contrib.auth.urls')),
    #path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset'), 
     #   'email_template': 'registration/password_reset_email.html'}, 
      #  name='password_reset'),
    #path('reset/password_reset_done', {'template_name': 'registration/password_reset_done.html'}, 
     #   name='password_reset_done'),
    #path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), 
     #   name='password_reset_confirm'),
    #path('reset/done', {'template_name': 'registration/password_reset_complete.html'}, 
     #   name='password_reset_complete'),
]