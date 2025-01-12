from django.urls import path

from .views import LoginRefreshView, LoginView, LogoutView, MyProfileView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("login/refresh/", LoginRefreshView.as_view(), name="login_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", MyProfileView.as_view(), name="profile"),
]
