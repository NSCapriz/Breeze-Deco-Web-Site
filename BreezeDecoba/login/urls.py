from django.urls import path
from login import views
from django.contrib.auth.views import LogoutView

# URLS views Login, Logout
urlpatterns = [
    path('accounts/login/', views.login_request, name="login"),
    path("accounts/logout/",LogoutView.as_view(template_name="login/logout.html"), name="Logout"),
]