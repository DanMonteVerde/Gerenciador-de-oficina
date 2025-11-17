from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.AccountCreateView.as_view(), name='register'),
]