from django.conf.urls import url

from .views import (blog_list,
                    blog_detail,

                    )


urlpatterns = [
    url(r'blogs/$', blog_list, name='blog-list'),
    url(r'^blogs/(?P<slug>[-\w\d]+)/$', blog_detail, name='blog-details'),
]