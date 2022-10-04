from django.shortcuts import render, redirect
from .models import Feed
from django.http import HttpResponse


# 메
def main(request):
  return render(request,'sns/index.html')
        
           

# 전체 피드 - 현지
def feed(request):
     return render(request, 'sns/index.html')

# 게시글 작성
def feed_create(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:  # 로그인 한 사용자라면
            return render(request, 'sns/index.html')
        
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')
        
    elif request == 'POST':
        user = request.user
        my_create = Feed()
        my_create.author = user
        my_create.content = request.POST.get('my-content',',')
        my_create.save()
        return redirect(request)
    
        
        

# @login-message_required
def feed_Update(request, pk):
    feed = Feed.objects.get(id=pk)
    if request.method == "POST":
       my_create = feed()
       my_create.author = User
       my_create.content = request.POSt.get('my-content',',')
       
       my_create.save()
       return redirect('sns/')
    else:
       return render (request, 'sns/index.html')

# 피드 삭제 - 승주님
def feed_delete(request):
    return render(request, 'sns/index.html')

# 댓글 -상