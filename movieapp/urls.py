from django.urls import path ,include 
from .views import UserRegistrationView,UserLoginView,LogoutView,MovieView,CartsView


urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('carts/',CartsView.as_view(),name='carts'),
    path('movies/',MovieView.as_view(),name='movie')
]