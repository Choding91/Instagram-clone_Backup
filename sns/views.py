from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Feed



# # 메인
def main(request):
  return render(request,'sns/index.html')
        
           

# # 전체 피드 - 현지
# def feed(request):
#      return render(request, 'sns/index.html')

# 게시글 작성
def feed_create(request):
    # if request.method == 'GET':
    #     return render(request, 'sns/index.html')  
    # #     my_create.auther = request.my_create.auther
    # #     if :  # 로그인 한 사용자라면
    # #         return render(request, 'sns/index.html')
        
    # #     else:  # 로그인이 되어 있지 않다면
    # #         return redirect('/sign-in')

    
    # 받은 데이터로 게시글 작성하기
    # 1. 데이터를 받기 = request.전달방법.get("데이터이름")
    # 2. 게시글 작서하기
    if request.method == 'GET':
        return redirect ( '/') 

    elif request.method == 'POST':
        my_auther= "승주"

        new_feed = Feed()
        new_feed.auther = my_auther
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

# # 피드 삭제 - 승주님
# def feed_delete(request):
#     return render(request, '/index.html')

# # 댓글 -상훈
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