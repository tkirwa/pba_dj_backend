from django.contrib import admin
from django.urls import path, include
from .views import RegistrationAPI, LoginAPI, UserAPI
# from knox import views as knox_views
from .views import LogoutView

urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('user/', UserAPI.as_view(), name='custom-user-detail'),
    path('login/', LoginAPI.as_view()),
    # path('logout/', knox_views.LogoutView.as_view(), name='knox_logout')
    # Include your knox URLs
    # path('login/', LoginView.as_view(), name='knox_login'),
    # path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logout/', LogoutView.as_view(), name='knox_logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(),
    #      name='knox_logoutall'),
    # path("accounts/auth/", include("knox.urls")),
]
