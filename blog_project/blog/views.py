from django.shortcuts import render, get_object_or_404
from .models import Blog, Author
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')
    
def index(request):
    data = Blog.objects.all()
    context = {
        'blogs': data
    }
    return render(request,'blog/index.html',context=context)



def show(request,article_id):
    data = get_object_or_404(Blog,id=article_id)
    context = {
        'article': data
    }
    return render(request,'blog/show.html',context=context)