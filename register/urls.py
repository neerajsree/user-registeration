from django.urls import path
from .views import *
urlpatterns = [
    path("login/",login,name="login"),
    path("registeration/",registeration,name="registeration"),
    path("userpage/",userpage,name="userpage"),
    path("logout/",logout,name="logout"),
    
]
