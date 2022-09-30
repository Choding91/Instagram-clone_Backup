from django.http import HttpResponse
from django.shortcuts import render

# 메인
def main(request):
    return render(request, 'sns/index.html')

# 전체 피드 - 현지
def feed(request):
    return render(request, 'sns/index.html')

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
