from django.conf.urls import url

from .views import post_list, post_create, post_comment_create, post_comment_delete, post_detail

app_name = 'post'

urlpatterns = [
    url(r'^$', post_list, name='list'), # /post
    url(r'^(?P<post_pk>\d+)/$', post_detail, name='detail'), #/post/1
    url(r'^create/$', post_create, name='create'), # /post/create/
    url(r'^(?P<pk>\d+)/comments/create/$', post_comment_create, name='comment_create'), #
    url(r'^comments/(?P<pk>\d+)/delete/$', post_comment_delete, name='comment_delete'), #
]