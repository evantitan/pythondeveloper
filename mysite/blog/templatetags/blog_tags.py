from django import template
from django.shortcuts import get_object_or_404
from blog.models import Post, Subject, Bookmark
from django.db.models import Count

register = template.Library()



@register.simple_tag
def get_first_post(topic=None):
    subject = Subject.objects.get(topic=topic)
    post = subject.chapters.all()[1]
    return post.get_absolute_url()

@register.simple_tag
def worked(user, post):
    if user.is_authenticated:
        if Bookmark.objects.filter(user=user, bookmark=post).exists():
            return True
    return False

'''
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')

@register.simple_tag
def all():
    #last_week_date = '2020-08-09'
    #all = Post.published.filter(publish__gte=last_week_date)
    #all = all[11]
    post = Post.objects.filter(title='python-introduction')
    return post

@register.simple_tag
def get_related_post(topic=None,  post_id=None):
    post = get_object_or_404(Post,id=post_id)
    dict = {}
    if topic == 'random':
        tags = post.tags.value_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=tags).exclude(id=post_id)
        dict.update({'similar_posts':similar_posts, 'random':True})
        return dict
    else:
        subject = post.subject()
        chapters = subject.chapters.all()
        dict.update({'all_chapters':chapters, 'random':False, 'subject':subject.title})
        return dict


@register.simple_tag
def get_all_comments(post, order):
    post = get_object_or_404(Post,id=post.id)
    order = 'created_on'
    if order == 'newest':
        order = '-created_on'
    all_comments = post.comments.filter(status='active').order_by('order') '''
