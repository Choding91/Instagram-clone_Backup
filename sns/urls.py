from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('feed/create/', views.feed_create, name='hello'),
    # path('feed/<int:pk>',views.feed_update, name='update' ) ,  
]