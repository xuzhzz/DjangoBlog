#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoBlog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
    '''
    from blog.models import Category, Tag, Post
    from django.utils import timezone
    from django.contrib.auth.models import User
    import datetime

    # 创建分类和标签
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Post.objects.all().delete()

    for i in range(5):
        c = Category(name='category'+str(i))
        c.save()
        t = Tag(name='tag'+str(i))
        t.save()
    user = User.objects.get(username='myuser')
    for i in range(10):
        p = Post(title='This is a title'+str(i), body='This is a long long long body for test' + str(i),
                 created_time=timezone.now() + datetime.timedelta(days = i),
                 modified_time=timezone.now() +  + datetime.timedelta(days = i),
                 category=Category.objects.get(name='category'+str(i//2)), author=user)
        p.save()
    '''

