from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return 'This is catagory: '+ self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return 'This is Tag: ' + self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True) # blank=True允许空值
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return 'This is post: ' + self.title
    class Meta:
        ordering = ['-created_time']
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def increase_view(self):
        self.views = self.views + 1
        self.save(update_fields=['views'])
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args, **kwargs)
