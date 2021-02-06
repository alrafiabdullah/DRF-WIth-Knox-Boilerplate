from django.urls import path, include
from knox import views as knox_views

from . import views

urlpatterns = [
    path('register', views.RegisterAPI.as_view(), name='register'),
    path('login', views.LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password', views.ChangePasswordView.as_view(),
         name='change-password'),
]
