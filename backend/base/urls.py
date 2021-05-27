from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path('api/users/register/', views.registerUser, name='register'),
    path('api/users/profile/', views.getUserProfile, name='user-profile'),
]
