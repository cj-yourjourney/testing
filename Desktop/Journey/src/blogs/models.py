from django.db import models
from tinymce import HTMLField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.urls import reverse

from django.dispatch import receiver

# Create your models here.

class Blog(models.Model):
    title   = models.CharField(max_length=200)
    content = HTMLField()
    slug    = models.SlugField(unique=True, null=True, blank=True)



    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug,})



def pre_save_blog_receiver(sender, instance, *args, **kwargs):

    slug = slugify(instance.title)

    instance.slug = slug



pre_save.connect(pre_save_blog_receiver, Blog)