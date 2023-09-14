from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def posts_home(request):
    post = Posts.objects.order_by('date')
    return render(request, 'posts/posts_home.html', {'post': post})


class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts/details_view.html'
    context_object_name = 'article'


class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'posts/create.html'

    form_class = PostsForm


class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'posts/posts-delete.html'
    success_url = '/posts'


def create(request):

    error = ''
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_home')
        else:
            error = 'Форма была неверной'

    form = PostsForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'posts/create.html', data)