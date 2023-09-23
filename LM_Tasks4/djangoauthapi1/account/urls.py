from django.urls import path
from account.views import UserRegestrationView, UserLoginView,  UserProfileView, UserListView

urlpatterns = [
    path("register/", UserRegestrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profiel"),
    path("userlist/", UserListView.as_view(), name="userlist"),
]
