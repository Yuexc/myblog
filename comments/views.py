from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import CommentForm
# from .models import Comment


def post_comment(request, post_pk):
    # 根据当前的文章ID获取文章实例
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            # 获取文章为post的comment列表
            comment_list = post.comment_set.all()
            context = {}
            context['post'] = post
            context['form'] = form
            context['comment_list'] = comment_list
            context['comment_num'] = comment_list.count()
            return render(request, 'blog/detail.html', context)
        return redirect(post)
