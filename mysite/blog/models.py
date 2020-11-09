from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings
from taggit.models import Tag


class PublishedManager(models.Manager):
    def get_quaryset(self):
        return super(PublishedManager,self).get_quaryset().filter(status='published')

class Subject(models.Model):
    topic = models.CharField(max_length=30, unique=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.topic


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published', 'Published'),
    )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='chapters', null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    description = models.TextField(null=True, blank=True)
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES, default='draft')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                    self.publish.month,
                                                    self.publish.day, self.slug])


    def get_all_comments(self):
        all_comments = self.comments.filter(status='active').order_by('-created_on')
        return all_comments

    def get_all_tags(self):
        tags_id = self.tags.values_list('id', flat=True)
        all_tags = Tag.objects.filter(id__in=tags_id)[:10]
        return all_tags

    def get_all_related_posts(self):
        if self.subject.topic != 'random':
            all_posts = self.subject.chapters.all()
        else:
            tags_id = self.tags.values_list('id', flat=True)
            all_posts = Post.published.filter(tags__in=tags_id).exclude(id=self.id)
        return all_posts




class Comment(models.Model):
    CHOICES = (('active','Active'),('inactive','Inactive'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=CHOICES, default='active')

    def __str__(self):
        return self.name



class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    bookmark = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='all_bookmark', null=True)
    bookmarked_on = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return 'bookmark for user {}'.format(self.user.first_name)



class Review(models.Model):
    CHOICES = [('o', '1'), ('tw', '2'), ('th', '3'), ('fo', '4'), ('fi', '5'),
                ('si', '6'), ('se', '7'), ('e', '8'), ('n', '9'), ('te', '10')]
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    suggestion = models.TextField(blank=True, null=True)
    rating = models.CharField(choices=CHOICES, max_length=2)

    def __str__(self):
        return self.name + self.rating
