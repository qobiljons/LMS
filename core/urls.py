from django.urls import path
from . import views


urlpatterns = [
    path("sign-up/", views.user_create_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("<str:username>/", views.user, name="profile"),
    path("<str:username>/edit/", views.user_edit, name="profile_edit"),  # replace 'edit_profile' with your actual view name.
]   