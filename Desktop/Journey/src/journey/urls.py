from django.conf.urls import url, include
from django.urls import include, path
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('landing_pages.urls','landing_page'), namespace='landing_pages')),
    url(r'^', include(('blogs.urls', 'blogs'), namespace='blogs')),
    url(r'^tinymce/', include('tinymce.urls')),

]
