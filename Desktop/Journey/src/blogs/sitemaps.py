from django.contrib.sitemaps import Sitemap

from .models import Blog



class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Blog.objects.all()

    # def lastmod(self, obj):
    #     return obj.pub_date





