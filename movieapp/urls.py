from django.urls import path ,include 
from .views import UserRegistrationView,UserLoginView,LogoutView,MovieViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies',MovieViewSet)

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('',include(router.urls))
]