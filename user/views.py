from re import fullmatch

from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .models import User
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

        if email == '':
            return Response(status=500, data=dict(message='이메일 주소를 입력해 주세요.'))

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response(status=500, data=dict(message='이메일 주소를 확인하세요.'))

        return Response(status=200, data=dict(message="해당 주소 '" + email + "'으로 로그인 링크를 보냈습니다."))

@login_required
def profile(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'user/profile.html')
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
        
    
        
    
# @login_required
# def profile_update(request):
#     if request == 'GET':
#         user
    
    
# class Profile(APIView):
#     def get(self, request):
#         user = User.objects.all()
#         email = request.session.get('email', None)
        
#         if email is None:
#             return render(request, 'user/signin.html')

#         user = User.objects.filter(email=email).first()
#         if user is None:
#             return render(request, 'user/signin.html')
        
#         else:
#             return render(request, 'user/profile.html', context=dict(user=user))
          
# class Profile_update(APIView):
#     def get(self, request):
#         user = User.objects.all()
#         email = request.session.get('email', None)
#         if email is None:
#             return render(request, 'user/signin.html')

#         user = User.objects.filter(email=email).first()
#         if user is None:
#             return render(request, 'user/signin.html')
        
#         else:    
#             return render(request, 'user/profile_update.html', context=dict(user=user))
        
#     def post(self, request):
        
#         name = request.data.get('name')
#         username = request.data.get('username')
#         website = request.data.get('website')
#         bio = request.data.get('bio')
#         email = request.data.get('email')
#         phone = request.data.get('phone')
        
#         REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
#         REGEX_PHONE = '010-\d{3,4}-\d{4}'

#         if name == '':
#             return Response(status=500, data=dict(message="변경할 이름을 입력해주세요."))
#         elif username == '':
#             return Response(status=500, data=dict(message="변경할 사용자 이름을 입력해주세요."))
#         elif website == '':
#             return Response(status=500, data=dict(message="변경할 웹사이트 주소를 입력해주세요."))
#         elif bio == '':
#             return Response(status=500, data=dict(message="변경할 정보를 입력해주세요."))
#         elif not fullmatch(REGEX_EMAIL, email):
#             return Response(status=500, data=dict(message="이메일 형식을 확인하세요."))
#         elif not fullmatch(REGEX_PHONE, phone):
#             return Response(status=500, data=dict(message="전화번호 형식을 확인하세요. '010-xxxx-xxxx'"))
#         else:
#             user_instance = request.user
#             user_instance.name = name
#             user_instance.username = username
#             user_instance.website = website
#             user_instance.bio = bio
#             user_instance.email = email
#             user_instance.phone = phone
#             user_instance.save()
#             return Response(status=200, data=dict(message="정보 수정에 성공했습니다."))


# class UpdateProfile(APIView):
#     def post(self, request):
#         email = request.session.get('email', None)
#         if email is None:
#             return render(request, 'user/signin.html')

#         user = User.objects.filter(email=email).first()
#         if user is None:
#             return render(request, 'user/signin.html')

#         file = request.FILES['file']
#         if file is None:
#             return Response(status=500)

#         uuid_name = uuid4().hex
#         save_path = os.path.join(MEDIA_ROOT, uuid_name)
#         with open(save_path, 'wb+') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)

#         user.thumbnail = uuid_name
#         user.save()

#         return Response(status=200, data=dict(uuid=uuid_name))


# class Profile(APIView):
#     def get(self, request):
#         email = request.session.get('email', None)
#         if email is None:
#             return render(request, 'user/signin.html')

#         user = User.objects.filter(email=email).first()
#         if user is None:
#             return render(request, 'user/signin.html')

#         feed_object_list = Feed.objects.filter(email=email).order_by('-id')
#         feed_list = []
#         row_feed_list = []
#         feed_count = feed_object_list.count()
#         for feed in feed_object_list:
#             like_count = FeedLike.objects.filter(feed_id=feed.id, is_like=True).count()
#             is_like = FeedLike.objects.filter(feed_id=feed.id, is_like=True, email=email).exists()
#             reply_count = Reply.objects.filter(feed_id=feed.id).count()
#             row_feed_list.append(dict(
#                 id=feed.id,
#                 profile_image=feed.profile_image,
#                 username=feed.username,
#                 image=feed.image,
#                 content=feed.content,
#                 like_count=like_count,
#                 is_like=is_like,
#                 reply_count=reply_count
#             ))

#             if len(row_feed_list) == 3:
#                 feed_list.append(dict(row_feed_list=row_feed_list))
#                 row_feed_list = []

#         if len(row_feed_list) > 0:
#             feed_list.append(dict(row_feed_list=row_feed_list))

#         following_count = Follow.objects.filter(follower=email, is_live=True).count()
#         follower_count = Follow.objects.filter(following=email, is_live=True).count()

#         bookmark_list = Bookmark.objects.filter(email=email, is_bookmarked=True).order_by('-id')
#         bookmark_feed_list = []
#         row_bookmark_feed_list = []
#         for bookmark in bookmark_list:
#             feed = Feed.objects.filter(id=bookmark.feed_id).first()
#             if feed is None:
#                 continue
#             like_count = FeedLike.objects.filter(feed_id=feed.id, is_like=True).count()
#             is_like = FeedLike.objects.filter(feed_id=feed.id, is_like=True, email=email).exists()
#             reply_count = Reply.objects.filter(feed_id=feed.id).count()
#             row_bookmark_feed_list.append(dict(
#                 id=feed.id,
#                 profile_image=feed.profile_image,
#                 user_id=feed.user_id,
#                 image=feed.image,
#                 content=feed.content,
#                 like_count=like_count,
#                 is_like=is_like,
#                 reply_count=reply_count
#             ))

#             if len(row_bookmark_feed_list) == 3:
#                 bookmark_feed_list.append(dict(row_bookmark_feed_list=row_bookmark_feed_list))
#                 row_bookmark_feed_list = []

#         if len(row_bookmark_feed_list) > 0:
#             bookmark_feed_list.append(dict(row_bookmark_feed_list=row_bookmark_feed_list))

#         return render(request,
#                       'chostagram/profile.html',
#                       context=dict(feed_list=feed_list,
#                                    bookmark_feed_list=bookmark_feed_list,
#                                    feed_count=feed_count,
#                                    following_count=following_count,
#                                    follower_count=follower_count,
#                                    user=user))