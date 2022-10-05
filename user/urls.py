from django.urls import path
from .views import Signin, Signup, Logout, Findpassword, Profile, Profile_update


urlpatterns = [

    path('signin', Signin.as_view(), name='signin'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', Logout.as_view(), name='logout'),
    path('findpassword', Findpassword.as_view(), name='findpassword'),
    path('profile', Profile.as_view(), name='profile'),
    path('profile_update/', Profile_update.as_view(), name='profile_update'),
]
