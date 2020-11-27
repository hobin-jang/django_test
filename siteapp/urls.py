from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('board/<int:board_id>', views.board, name="board"),
    path('', views.home, name="home"),
    path('detail/<int:contents_id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('detail/<int:contents_id>/delete', views.delete, name="delete"),
    path('detail/<int:contents_id>/update', views.update, name="update"),
    path('comment_delete/<int:comment_id>', views.comment_delete, name="comment_delete"),
    path('recomment/<int:comment_id>', views.recomment, name="recomment"),
    path('recomment_delete/<int:recomment_id>',views.recomment_delete, name="recomment_delete"),
    path('contents_like/<int:contents_id>',views.like, name="contents_like"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)