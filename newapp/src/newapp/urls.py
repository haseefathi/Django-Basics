"""newapp URL Configuration

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
from django.contrib import admin
from Blog.views import article_form_view, HomeDetailView,HomeListView,MyListView,HomeCreateView, HomeUpdateView,HomeDeleteView
from django.urls import path, include

urlpatterns = [
    path('art/',HomeDetailView.as_view(template_name='home.html') ),
    path('art/<int:id>/', HomeDetailView.as_view(), name="home-detail-view"),
    path('art/<int:id>/update',HomeUpdateView.as_view()),
    path('art/<int:id>/delete',HomeDeleteView.as_view()),
    path('art/homelist/',HomeListView.as_view() , name = "home-list"),
    path('art/homecreate/',HomeCreateView.as_view() ),
    path('article/', include('Blog.urls')),
    path('form/',article_form_view ),
    path('admin/', admin.site.urls),
]
