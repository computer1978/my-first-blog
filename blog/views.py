from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

def add_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
            form = PostForm(data=request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                return redirect('blog:post_list')
    context = {'form': form}
    return render(request, 'blog/add_post.html', context)

def delete_post(reuqest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog:post_list')
