from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Feed
from .models import FeedComment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# # 메인
def main(request):
    user = request.user.is_authenticated
    if user:
        all_feed = Feed.objects.all().order_by('-created_at')
        return render(request, 'sns/index.html', {'feeds': all_feed})
    else:
        return redirect('/signin')
  
# 특정 피드 - 현지
@login_required
def feed_detail(request,id):
    target_feed = Feed.objects.get(id=id)
    each_comment = FeedComment.objects.filter(feed_id=id)
    
    return render(request, 'sns/feed.html',  {'feed': target_feed , 'comments':each_comment })

# 피드 작성 - 승주님
@login_required
def feed_create(request):
    if request.method == 'GET':
        return redirect ('/') 

    elif request.method == 'POST':
        my_author= request.user

        new_feed = Feed()
        new_feed.author = my_author
        new_feed.content = request.POST.get('my-content')
        new_feed.save()

        # 피드 작성후 작성한 피드 상세페이지로 이동
        new_feed_id = Feed.objects.last().id
        messages.add_message(request,messages.SUCCESS,'게시글이 작성되었습니다.')
        return redirect (f'/feed/{new_feed_id}')

# 피드 수정 - 승주님       
@login_required
def feed_update(request, id):
    feed = Feed.objects.get(id=id)
    if request.method == 'POST':
        update_feed = feed()
        update_feed.auther= update_feed
        update_feed= request.POST.get('my-content')
        
        update_feed.save()
        
        return render(request, 'index.html')
    else:
       return redirect ('/') 

# 피드 삭제 - 현지님
@login_required
def feed_delete(request,id):
    target_feed = Feed.objects.get(id=id)
    # 게시물 작성자, 관리자만 삭제 가능
    if (target_feed.author == request.user.username):
        target_feed.delete()
        messages.add_message(request,messages.SUCCESS,'삭제되었습니다.')
        return redirect('/')
    elif request.user.is_staff:
        target_feed.delete()
        messages.add_message(request,messages.SUCCESS,'관리자 권한으로 삭제되었습니다.')
        return redirect('/')
    else:
        messages.add_message(request,messages.ERROR,'본인 게시글이 아닙니다.')
        return redirect(f'/feed/{id}') 


# 댓글 - 상훈
@login_required
def write_comment(request, id):
    if request.method == 'POST':
        # request 데이터 받기
        form_content = request.POST.get("comment")
        form_author = request.user
        form_feed =  Feed.objects.get(id = id) 

        # DB저장
        new_fc = FeedComment(); 
        new_fc.content = form_content
        new_fc.author = form_author
        new_fc.feed = form_feed
        new_fc.save()

        return redirect(f'/feed/{id}')


@login_required
def delete_comment(request, id): 

    delete_comment = FeedComment.objects.get(id=id)
    current_feed_id = delete_comment.feed.id
    # 삭제 권한
    # 1. 댓글을 작성한 사람이 현재 로그인 사람이면
    #  1-1. 댓글의 작성자(delete_comment.author)와 현재 로그인한 사람(request.user)가 같으면
    # 2. 관리자 계정으로 로그인했을때
    #   2-1. 지금 로그인한 계정(request.user)가 관리자인지(is_staff)
    if delete_comment.author == request.user.username:
        #삭제 가능
        delete_comment.delete()
        return redirect(f'/feed/{current_feed_id}')
    
    elif request.user.is_staff:
        delete_comment.delete()
        messages.add_message(request,messages.SUCCESS,'관리자권한으로 댓글을 삭제했습니다.')
        return redirect(f'/feed/{current_feed_id}')
    else:
        #삭제 안됨
        messages.add_message(request,messages.ERROR,'댓글을 삭제할 수 없습니다.')
        return redirect(f'/feed/{current_feed_id}')
       
