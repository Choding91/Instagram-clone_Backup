from django.http import HttpResponse
from django.shortcuts import render
from .models import Feed

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
