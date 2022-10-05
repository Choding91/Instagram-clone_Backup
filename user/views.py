from re import fullmatch

from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import User
from sns.models import Feed
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

class Signin(APIView):
    def get(self, request):
        return render(request, 'user/signin.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if email == '':
            return Response(status=500, data=dict(message='이메일 주소를 입력해 주세요.'))
        elif user is None:
            return Response(status=500, data=dict(message='이메일 주소가 잘못되었습니다.'))
        elif password == '':
            return Response(status=500, data=dict(message='비밀번호를 입력해 주세요.'))
        elif check_password(password, user.password) is False:
            return Response(status=500, data=dict(message='비밀번호가 잘못되었습니다.'))
        else:
            me = auth.authenticate(request, username=user, password=password)
            auth.login(request, me)
            request.session['loginCheck'] = True
            request.session['email'] = user.email
            return Response(status=200, data=dict(message='로그인에 성공했습니다.'))


class Signup(APIView):
    def get(self, request):
        return render(request, 'user/signup.html')

    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        username = request.data.get('username')
        name = request.data.get('name')

        # 회원가입 정규식 체크
        REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        REGEX_PASSWORD = '^(?=.*[\d])(?=.*[a-zA-Z])(?=.*[!@#$%^&*()])[\w\d!@#$%^&*()]{8,16}$'

        if User.objects.filter(email=email).exists():
            return Response(status=500, data=dict(message="해당 이메일 주소가 존재합니다."))
        elif User.objects.filter(username=username).exists():
            return Response(status=500, data=dict(message="사용자 이름 '" + username + "'이(가) 존재합니다."))
        elif not fullmatch(REGEX_EMAIL, email):
            return Response(status=500, data=dict(message="이메일 형식을 확인하세요."))        
        elif not fullmatch(REGEX_PASSWORD, password):
            return Response(status=500, data=dict(message="비밀번호는 8~16자리의 영문, 숫자, 특수문자 조합만 가능합니다."))
        else:
            make_password(password)
            User.objects.create(password=make_password(password),
                                email=email,
                                username=username,
                                name=name)
            return Response(status=200, data=dict(message="회원가입에 성공했습니다."))


class Logout(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, 'user/signin.html')


class Findpassword(APIView):
    def get(self, request):
        return render(request, 'user/findpassword.html')

    def post(self, request):
        email = request.data.get('email', None)
        user = User.objects.filter(email=email).first()

        if email == '':
            return Response(status=500, data=dict(message='이메일 주소를 입력해 주세요.'))
        elif user is None:
            return Response(status=500, data=dict(message='이메일 주소를 확인하세요.'))
        else:
            return Response(status=200, data=dict(message="해당 주소 '" + email + "'으로 로그인 링크를 보냈습니다."))

@login_required
def profile(request):
    if request.method == 'GET':
        
        user = request.user
        my_feed = Feed.objects.filter(author=user.username)
        
        if user:
            return render(request, 'user/profile.html', {'user': user, 'my_feed': my_feed})
        else:
            return redirect('/')

@login_required
@csrf_exempt    
def profile_update(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'user/profile_update.html')
        else:
            return redirect('/')
    
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        website = request.POST.get('website', '')
        bio = request.POST.get('bio', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        
        REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        REGEX_PHONE = '010-\d{3,4}-\d{4}'

        if name == '':
            return render(request, 'user/profile_update.html', {'error': '이름을 입력해주세요!'})
        elif username == '':
            return render(request, 'user/profile_update.html', {'error': '사용자 이름을 입력해주세요!'})
        elif website == '':
            return render(request, 'user/profile_update.html', {'error': '웹사이트 주소를 입력해주세요!'})
        elif bio == '':
            return render(request, 'user/profile_update.html', {'error': '소개를 입력해주세요!'})
        elif not fullmatch(REGEX_EMAIL, email):
            return render(request, 'user/profile_update.html', {'error': '이메일을 입력해주세요!'})
        elif not fullmatch(REGEX_PHONE, phone):
            return render(request, 'user/profile_update.html', {'error': '전화번호을 입력해주세요!'})
        else:
            user_instance = request.user
            user_instance.name = name
            user_instance.username = username
            user_instance.website = website
            user_instance.bio = bio
            user_instance.email = email
            user_instance.phone = phone
            user_instance.save()
            return redirect('/profile')
