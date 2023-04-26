from django.urls import path, include
from . import views

app_name = "users"
urlpatterns = [
    # default auth urls
    path("", include("django.contrib.auth.urls")),
    # Registration page for new users
    path("register/", views.register, name="register"),
    # a page for users to create profile
    path("user_profile/<int:user_id>/", views.user_profile, name="user_profile"),
]
