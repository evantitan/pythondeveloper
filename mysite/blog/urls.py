from django.urls import path, reverse_lazy
from .import views

app_name = 'blog'

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail, name='post_detail'),
    path('tag/<slug:tag_name>/',views.post_list_by_tag, name='post_list_by_tag'),
    path('search/',views.post_search, name='post_search'),
    path('<int:id>/save/',views.bookmark_post, name='bookmark_post'),
    path('bookmarks/',views.bookmark, name='bookmark'),
    path('delete/<int:id>',views.delete_bookmark, name='delete_bookmark'),
    path('<int:id>/post_comment/',views.post_comment, name='post_comment'),
    path('suggestion/', views.UserReview.as_view(success_url=reverse_lazy('blog:thanks')), name='review'),
    path('thanks/',views.thanks, name='thanks')
]
