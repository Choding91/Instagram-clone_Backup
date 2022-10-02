from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Feed
from .models import FeedComment

# 메인
def main(request):
    all_feed = Feed.objects.all().order_by('-created_at')
    return render(request, 'sns/index.html', {'feeds': all_feed})

# 특정 피드 - 현지
def feed_detail(request,id):
    target_feed = Feed.objects.get(id=id)
    return render(request, 'sns/feed.html',  {'feed': target_feed})

# 피드 작성 - 현지
def feed_create(request):
    return render(request, 'sns/index.html')

# 피드 업데이트 - 승주님
def feed_update(request):
    return render(request, 'sns/index.html')

# 피드 삭제 - 승주님
def feed_delete(request):
    return render(request, 'sns/index.html')

# 댓글 - 상훈

def detail_comment(request, id):
    my_feed = Feed.objects.get(id=id)
    feed_comment = FeedComment.objects.filter(feed_id=id).order_by('-created_at')
    return render(request,'sns/commentdetail.html',{'sns':my_feed,'comment':feed_comment})


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
    comment = FeedComment.objects.get(id=id)
    current_feed = comment.feed.id
    comment.delete()
    return redirect('/sns/'+str(current_feed))