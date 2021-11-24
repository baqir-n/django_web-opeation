from django.contrib import admin  
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.welcome, name='home'),
    path('emp', views.emp),
    path('show',views.show,name='show'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('login/',views.login, name='login'),
    path('register',views.register,name='register'),
    path('sendmail/',views.send_mail, name='sendmail'),
    path('entercode/<int:id>', views.enter_code),
    path('updatepass/<int:id>', views.enter_pass),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm')
]