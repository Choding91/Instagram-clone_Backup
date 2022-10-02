from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('feed/<int:id>', views.feed_detail, name='feed_detail'),
    # path('sns/', views.feed, name='sns'),
    # path('sns/detail/', views.detail_feed, name='detail_feed'),
    # path('sns/delete/<int:id>', views.feed_delete, name='delete_feed'),
    path('sns/comment/detail/', views.detail_comment, name='detail_comment'),
    path('sns/comment/write/<int:id>', views.write_comment, name='write_comment'),
    path('sns/comment/delete/<int:id>', views.delete_comment, name='delete_comment'),
]
