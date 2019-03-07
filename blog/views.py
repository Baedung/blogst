from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects # 모델로부터 객체목록을 전달받을 수 있다.
    # 이러한 객체목록을 쿼리셋이라고 함.
    return render(request, 'home.html', {'blogs' : blogs} )

    # home 함수와 detail함수의 차이점을 분명히 구분해야한다.

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    # 2가지 인자를 받는데 Blog 클래스의 몇번째 객체를 받아오는지 
    return render(request, 'detail.html', {'blog':blog_detail})

