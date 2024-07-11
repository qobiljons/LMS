from django.urls import path
from . import views


urlpatterns = [
    path("sign-up/", views.user_create_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
]