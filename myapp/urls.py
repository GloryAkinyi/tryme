from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('inner/', views.inner, name='inner'),
    path('join/', views.join, name='join'),
    path('details/', views.details, name='details'),
]
