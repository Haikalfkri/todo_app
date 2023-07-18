from django.urls import path
from account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.FormLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register", views.RegisterView.as_view(), name="register")
]
