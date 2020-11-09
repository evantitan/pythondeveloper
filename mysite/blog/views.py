from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Subject, Comment, Bookmark
from .forms import CommentForm, SearchForm, UserCommentForm, ReviewForm
from django.views.generic.edit import CreateView
from taggit.models import Tag
from django.urls import reverse
from django.db.models import Count,Q
import csv
from mysite import settings
from django.contrib.auth.decorators import login_required


def home(request):
    authenticated = is_authenticated(request.user)
    csv_file = open('static/files/python.csv')
    csv_reader = csv.reader(csv_file)
    data = []
    for row in csv_reader:
        data.append(row)

    agent = find_agent(request.user_agent)
    template = '{}/home.html'.format(agent)
    all_tags = Tag.objects.all()[:22]
    subject = get_object_or_404(Subject, topic='introduction')
    recent_posts = Post.published.order_by('-publish').exclude(subject = subject)[:12]
    home_post = Post.objects.filter(title='python-introduction')[:1][0]
    return render(request, template, {'all_tags':all_tags,
                                        'recent_posts':recent_posts,
                                        'data':data,
                                        'authenticated':authenticated,
                                        'home_post':home_post
                                            })



def post_detail(request, year, month, day, post):
    post_slug=post
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    agent = find_agent(request.user_agent)
    bookmarked = is_bookmarked(user=request.user, bookmark=post)
    comment_form = CommentForm()
    authenticated = is_authenticated(request.user)
    if authenticated:
        comment_form = UserCommentForm()

    dict = {'post':post,
            'comment_form':comment_form,
            'is_bookmarked':bookmarked,
            'authenticated':authenticated
            }

    template = '{}/detail.html'.format(agent)
    if post.subject.topic == 'random':
        dict.update({'is_topic': False})
    else:
        dict.update({'is_topic':True})
    return render(request, template, dict)



def post_list_by_tag(request, tag_name):
    agent = find_agent(request.user_agent)
    template = '{}/post_list_by_tag.html'.format(agent)
    tag = get_object_or_404(Tag, name=tag_name)
    tag_id = tag.id
    all_tags = Tag.objects.all()[:22]
    all_posts = Post.published.all().filter(tags=tag_id)
    return render(request, template, {'all_posts':all_posts,
                                        'all_tags':all_tags,
                                        'tag':tag})



def post_search(request):
    agent = find_agent(request.user_agent)
    template = '{}/search_result.html'.format(agent)
    form = SearchForm()
    query = request.GET.get('search')
    subject = get_object_or_404(Subject, topic='introduction')
    results = Post.published.filter(Q(title__contains=query) | Q(body__contains = query)).exclude(subject=subject)
    all_tags = Tag.objects.all()[:22]
    return render(request, template,  {'query':query,
                                        'results':results,
                                        'all_tags':all_tags})



def bookmark_post(request, id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' %(settings.lOGIN_URL, request.META['HTTP_REFERER']))
    else:
        post = get_object_or_404(Post, id=id)
        is_bookmark = Bookmark.objects.filter(user=request.user, bookmark=post)
        if is_bookmark:
            is_bookmark.delete()
            return redirect(request.META['HTTP_REFERER'])
        Bookmark.objects.create(user=request.user, bookmark=post)
        return redirect(request.META['HTTP_REFERER'])



@login_required(login_url='account:login')
def bookmark(request):
    agent = find_agent(request.user_agent)
    template = '{}/bookmark_post.html'.format(agent)
    all_bookmarks = Bookmark.objects.filter(user=request.user).order_by('-bookmarked_on')

    return render(request, template, {'all_bookmarks':all_bookmarks})




@login_required(login_url='account:login')
def delete_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, user=request.user, id = id)
    if bookmark:
        bookmark.delete()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponse("Selected post has been deleted!")


def post_comment(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = UserCommentForm(request.POST)
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.user = None
                new_comment.save()
                return redirect(request.META['HTTP_REFERER'])


class UserReview(CreateView):
    form_class = ReviewForm
    template_name = 'pc/review.html'

def thanks(request):
    return render(request, 'pc/thanks.html')


def find_agent(user_agent):
    if user_agent.is_mobile:
        agent = 'mobile'
    else:
        agent = 'pc'
    return agent

def is_bookmarked(user, bookmark):
    if user.is_authenticated:
        if Bookmark.objects.filter(user=user, bookmark=bookmark).exists():
            return True
    return False

def is_authenticated(user):
    if user.is_authenticated:
        return True
    return False


def test(request):
    return render(request, 'pc/test.html', {})
