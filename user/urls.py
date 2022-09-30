from django.urls import path
from . import views

urlpatterns = [
    path('user/signin/', views.signin_view, name='signin')
]
