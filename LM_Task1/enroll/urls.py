from django.urls import path
from . import views

urlpatterns = [
    path('signUp/', views.sign_Up, name="signUp"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('changepass/', views.user_change_pass, name='changepass'),
    path('changepass1/', views.user_change_pass1, name="changepass1"),
    path('', views.home, name="HomePage"),
    path('editprofile/', views.edit_profile, name="editprofile"),
]
