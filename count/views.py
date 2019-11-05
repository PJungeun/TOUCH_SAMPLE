from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.


def main(request):
    posts=Post.objects.all()
    return render(request, 'count/main.html')


def like(request, post_pk):
    post= get_object_or_404(Post, pk=post_pk)
    return redirect('main')

count_t = 0
def count(request):
    global count_t # 바깥영역의 변수를 사용할 때 global
    count_t = count_t + 1 # 접속할 때마다 방문자 1 증가
    
    return render(request, 'count/count.html', {'cnt': count_t })