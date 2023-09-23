from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('signup/', views.custom_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name="HomePage"),
]
