from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('feed/<int:id>', views.feed_detail, name='feed_detail'),
    path('feed/create/', views.feed_create, name='feed_create'),
    path('feed/update/<int:id>',views.feed_update, name='feed_update'),
    path('feed/delete/<int:id>', views.feed_delete, name='feed_delete'),
    path('sns/comment/write/<int:id>', views.write_comment, name='write_comment'),
    path('sns/comment/delete/<int:id>', views.delete_comment, name='delete_comment'),
]