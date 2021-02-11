"""odds_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from odds_news.news.views import NewsAPIView
# from odds_news.news.views import NewsAPISimpleView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from news.views import (
    news_view, NewsView, NewsAPIView, 
    NewsAPISimpleView,
    NewsViewSet
)

# add this for model viewsets
router = routers.DefaultRouter()
router.register(r'newsx', NewsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('news/', news_view),
    path('news1/', NewsView.as_view()),
    path('news-api/', NewsAPIView.as_view()),
    path('news-simple-view', NewsAPISimpleView.as_view())
]
