# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
import markdown
from comments.forms import CommentForm


# 博客主页
def index(request):
    context = {}
    post_list = Post.objects.all().order_by('-created_time')    # -表示逆序
    context['post_list'] = post_list
    return render(request, 'blog/index.html', context)


# 博客详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {}
    context['post'] = post
    context['comment_list'] = comment_list
    context['comment_num'] = comment_list.count()
    context['form'] = form
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by('-created_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
