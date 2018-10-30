from django import template
from ..models import Post, Category

register = template.Library()


# 最新文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[: num]


# 时间归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 类目归档
@register.simple_tag
def get_categories():
    return Category.objects.all()
