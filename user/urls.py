from django.urls import path
from .views import RegisterView, LoginView, UserDetailView

urlpatterns = [
    path('auth/register', RegisterView.as_view(), name='user-register'),
    path('auth/login', LoginView.as_view(), name='user-login'),
    path('api/users/<uuid:userId>', UserDetailView.as_view(), name='user-detail'),
]