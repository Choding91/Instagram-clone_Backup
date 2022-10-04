from django.urls import path
from .views import Signin, Signup, Logout, Findpassword

urlpatterns = [
    path('signin', Signin.as_view(), name='signin'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', Logout.as_view(), name='logout'),
    path('findpassword', Findpassword.as_view(), name='findpassword')
]