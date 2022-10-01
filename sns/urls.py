from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('feed/<int:id>', views.feed_detail, name='feed_detail'),
]
