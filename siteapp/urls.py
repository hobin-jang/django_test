from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:contents_id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    #path('detail/<int:contents_id>/',views.create_comment, name="create_comment"),
]