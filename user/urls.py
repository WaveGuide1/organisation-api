from django.urls import path
from .views import RegisterView, LoginView, UserDetailView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('api/user/<uuid:userId>/', UserDetailView.as_view(), name='user-detail'),
]