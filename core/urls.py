from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("sign-up/", views.user_create_view, name="signup"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change_custom"),
    path("<str:username>/", views.user, name="profile"),
    path("<str:username>/edit/", views.user_edit, name="profile_edit"),  # replace 'edit_profile' with your actual view name.
]   