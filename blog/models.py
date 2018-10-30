from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Django要求模型必须继承models.Model类


# 博客的类目
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 博客的标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 博客类
class Post(models.Model):
    # 标题
    title = models.CharField(max_length=70)

    # 正文
    body = models.TextField()

    # 创建时间和更新时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，允许空值 blank = true
    excerpt = models.CharField(max_length=200, blank=True)

    # 文章类目，一对多
    category = models.ForeignKey(Category)

    # 文章标签，多对多
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者， 一对多
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
