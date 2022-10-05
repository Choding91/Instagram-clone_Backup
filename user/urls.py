from django.urls import path
from .views import Signin, Signup, Logout, Findpassword
from . import views


urlpatterns = [
    path('signin', Signin.as_view(), name='signin'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', Logout.as_view(), name='logout'),
    path('findpassword', Findpassword.as_view(), name='findpassword'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
]