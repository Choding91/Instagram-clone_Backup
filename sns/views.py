from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Feed
from .models import FeedComment
# # 메인
def main(request):
    all_feed = Feed.objects.all().order_by('-created_at')
    return render(request, 'sns/index.html', {'feeds': all_feed})
  
# 특정 피드 - 현지
def feed_detail(request,id):
    target_feed = Feed.objects.get(id=id)
    each_comment = FeedComment.objects.filter(feed_id=id)
    
    return render(request, 'sns/feed.html',  {'feed': target_feed , 'comments':each_comment })

# 피드 작성 - 승주님
def feed_create(request):
    # if request.method == 'GET':
    #     return render(request, 'sns/index.html')  
    # #     my_create.auther = request.my_create.auther
    # #     if :  # 로그인 한 사용자라면
    # #         return render(request, 'sns/index.html')
        
    # #     else:  # 로그인이 되어 있지 않다면
    # #         return redirect('/sign-in')

    if request.method == 'GET':
        return redirect ( '/') 

    elif request.method == 'POST':
        my_author= "승주"

        new_feed = Feed()
        new_feed.author = my_author
        new_feed.content = request.POST.get('my-content')
        new_feed.save()

        return redirect ( '/') 
        
# # @login-message_required
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
def feed_delete(request,id):
    target_feed = Feed.objects.get(id=id)
    target_feed.delete()
    return redirect('/')

# 댓글 - 상훈

def write_comment(request, id):
    if request.method == 'POST':
        # request 데이터 받기
        form_content = request.POST.get("comment")
        form_author = "손상훈"
        form_feed =  Feed.objects.get(id = id) 

        # DB저장
        new_fc = FeedComment(); 
        new_fc.content = form_content
        new_fc.author = form_author
        new_fc.feed = form_feed
        new_fc.save()

        return redirect(f'/feed/{id}')

def delete_comment(request, id): 
    delete_comment = FeedComment.objects.get(id=id) 
    current_feed_id = delete_comment.feed.id
    delete_comment.delete()
    
    return redirect(f'/feed/{current_feed_id}')