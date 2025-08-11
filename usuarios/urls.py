from django.urls import path, re_path
from . import views

urlpatterns = [
    
    # API usuarios
    re_path('api/signup', views.signUp),
    re_path('api/login', views.login),
    re_path('api/test_token', views.testToken),
    
]
