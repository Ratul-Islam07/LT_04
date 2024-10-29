# views.py
from django.shortcuts import render
from posts.models import Post
from django.db.models import Q

def home(request):
    find = request.GET.get('search') 
    if find:
        data = Post.objects.filter(
            Q(title__icontains=find) | Q(category__name__icontains=find)
        )  
    else:
        data = Post.objects.all()
    
    return render(request, 'home.html', {'data': data})
