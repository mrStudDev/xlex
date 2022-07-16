from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('post-single', args=(str(self.id)))
        return reverse('home')


class PostsXlex(models.Model):
    title = models.CharField(max_length=120)
    img_destaque = models.ImageField(upload_to='images/', default=1, null=True, blank=True)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default="Xlex-Undefined")
    content = RichTextUploadingField(blank=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.CharField(max_length=200)
    key_word = models.CharField(max_length=50)
    meta_description = models.TextField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('post-single', args=(str(self.id)))
        return reverse('home')
