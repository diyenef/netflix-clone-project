from django.urls import path
from .views import HomeView, SignupView, BrowseView, NetflixLoginView, NetflixLogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('browse/', BrowseView.as_view(), name='browse'),
    path('login/', NetflixLoginView.as_view(), name='login'),
    path('logout/', NetflixLogoutView.as_view(), name='logout'),
]
