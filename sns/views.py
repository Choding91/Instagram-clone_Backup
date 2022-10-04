from django.shortcuts import render, redirect
from rest_framework.views import APIView
from user.models import User
# from django.http import HttpResponse


# def main(request):
#     return render(request, 'sns/index.html')


class Index(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        if email is None:
            return render(request, 'user/signin.html')

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, 'user/signin.html')

        else:
            return render(request, 'sns/index.html')