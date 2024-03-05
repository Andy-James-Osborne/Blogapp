from django.shortcuts import render, redirect
from .models import Post, Category1, Category2, Comment
from django.contrib import messages

# Create your views here.

def home(request):
    get_all_post = Post.objects.all()
    get_all_categories_in_category1 = Category1.objects.all()
    get_all_categories_in_category2 = Category2.objects.all()
    context = {
        'posts': get_all_post,
        'category1': get_all_categories_in_category1,
        'category2': get_all_categories_in_category2,
    }
    return render(request, 'main/index.html', context)

def post_detail(request, slug):
    get_post = Post.objects.get(slug=slug)
    get_all_comments = Comment.objects.filter(post=get_post)
    number_of_comments = 0
    for i in get_all_comments:
        number_of_comments += 1
    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        new_comment = Comment(name=name, post=get_post, body=body)
        new_comment.save()
        messages.success(request, 'Your comment has been added successfully.')
        return redirect('post_detail', slug=slug)
    get_post = Post.objects.get(slug=slug)
    context = {
        'post': get_post,
        'comments': get_all_comments,
        'number_of_comments': number_of_comments,
    }
    return render(request, 'main/article.html', context)
