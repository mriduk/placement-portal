from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from registers.views import * 
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView

from . import views

urlpatterns = [
    path('signin/',views.signin,name='signin'),
    path('<slug:username>/profile/',views.profile,name='profile'),
    path('excel/',views.download_excel_data,name='download_excel_data'),
    
    # path('update/',views.update,name='update'),
    # path('<slug:pk>/', profile.as_view(), name='profile'),
    # url('profile/', profile.as_view(), name='profile'),  
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    url(r'^reset_password/$',PasswordResetView.as_view(),name='reset_password'),
    url(r'^reset_password/done/$',PasswordResetDoneView.as_view(),name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url(r'^reset_password/complete/$',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('test/', views.test,name='test'),
    # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

   
    

    
    
]

