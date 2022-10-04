from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('sns/index.html',views.feed_create, name='create'),
]   