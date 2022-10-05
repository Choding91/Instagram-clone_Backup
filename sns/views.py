from django.shortcuts import render, redirect
from rest_framework.views import APIView
from user.models import User


class Index(APIView):
    def get(self, request):
        email = request.session.get('email', None)
        user = User.objects.filter(email=email).first()

        if email is None:
            return redirect('signin')
        elif user is None:
            return redirect('signin')
        else:
            return render(request, 'sns/index.html')