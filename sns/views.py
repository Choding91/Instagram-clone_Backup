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

    # FeedComment 모델을 객체화 해서 filter(검색)한다.
    # Model.objects.filter("검색할 필드이름"="검색값")
    # 1. 피드 각각에 작성된 댓글을 찾고싶은것이다.
    # 2. FeedComment에서 피드를 id 값으로 찾기
    each_comment = FeedComment.objects.filter(feed_id=id)

    # M-V-T : 모델에서 데이터 가져와서 View에서 데이터를 처리하고 Template에서 데이터를 뿌려준다.
    return render(request, 'sns/feed.html',  {'feed': target_feed , 'comments':each_comment })

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
    # 댓글 삭제 기능
    # 1. 내가 클릭한 댓글(FeedComment) 삭제
    # 1-1. 내가 클릭한 댓글(FeedComment)? id값으로 구분
    # 1-2. id값으로 댓글을 찾기
    # 1-3. 찾은 댓글 삭제
    # Model.objects.get("검색할 필드이름"="검색값") 
    
    delete_comment = FeedComment.objects.get(id=id) # 게시글댓글의 객체를 가져온다. 고유값(id)기준으로.
    current_feed_id = delete_comment.feed.id # 삭제할 댓글의 게시글의 고유값(id)
    delete_comment.delete() #댓글 삭제
    
    # 2. 삭제 끝냈으니깐 원래 있는 게시글(current_feed_id: 게시글 id값) 로 이동
    return redirect(f'/feed/{current_feed_id}')