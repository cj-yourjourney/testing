from django.conf.urls import url

from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap


from .views import (blog_list,
                    blog_detail,

                    )


sitemaps = {
    "blogs" : BlogSitemap,
}



urlpatterns = [
    url(r'blogs/$', blog_list, name='blog-list'),
    url(r'^blogs/(?P<slug>[-\w\d]+)/$', blog_detail, name='blog-details'),
    url(r'^blogs/sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

]