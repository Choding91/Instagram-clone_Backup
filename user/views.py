from django.shortcuts import render

# Create your views here.
def signin_view(request):
    return render(request, 'user/signin.html')