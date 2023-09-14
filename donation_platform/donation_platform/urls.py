"""donation_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import UsersListView, UsersCreateView, UsersDetailView, UserSearchView, UserLoginView
from administrator.views import AdministratorListView, AdministratorDetailView, AdministratorSearchView
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('users/', UsersListView.as_view(), name='user-list'),
    path('users/create/', UsersCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='user-detail'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('administrators/', AdministratorListView.as_view(), name='administrator-list'),
    path('administrators/<int:pk>/', AdministratorDetailView.as_view(), name='administrator-detail'),
    path('administrators/search/', AdministratorSearchView.as_view(), name='administrator-search'),

]
