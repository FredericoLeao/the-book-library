"""thebooklibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/books/', include('book.urls_api')),
    path('api/authors/', include('book.urls_authors_api')),
    path('api/categories/', include('book.urls_categories_api')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/login/refresh/', TokenObtainPairView.as_view()),
    path('api/accounts/', include('account.urls_api')),
]
