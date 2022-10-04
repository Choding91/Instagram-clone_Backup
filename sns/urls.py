from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('feed/<int:id>', views.feed_detail, name='feed_detail'),
    path('feed/delete/<int:id>', views.feed_delete, name='feed_detail'),
]
