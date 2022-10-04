from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('feed/<int:id>', views.feed_detail, name='feed_detail'),
    path('feed/create/', views.feed_create, name='hello'),
    # path('feed/<int:pk>',views.feed_update, name='update' ) ,  
    path('feed/delete/<int:id>', views.feed_delete, name='feed_detail'),
]

