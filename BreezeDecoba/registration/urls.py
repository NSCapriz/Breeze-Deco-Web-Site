from django.urls import path
from registration import views

urlpatterns = [
    path('accounts/signup/', views.registro, name="registro"),
]
