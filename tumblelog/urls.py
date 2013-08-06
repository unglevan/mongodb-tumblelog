from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from tumblelog.models import Post
from tumblelog.views import PostDetailView
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all(),
        context_object_name="posts_list"),
        name="home"
    ),
    url(r'^post/(?P<slug>[a-zA-Z0-9-]+)/$', PostDetailView.as_view(
        queryset=Post.objects.all(),
        context_object_name="post"),
        name="post"
    ),
    url(r'^admin/', include(admin.site.urls)),
)