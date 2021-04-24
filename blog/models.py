from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils import timezone



class PostManager(models.Manager):

    def published(self):
        now = timezone.now()
        return self.filter(Q(publish_date__lte=now)|Q(publish_date=None))


class Tag(models.Model):

    name = models.SlugField(
        max_length=32,
        db_index=True,
        unique=True,
        help_text='Tag name'
    )

    def __str__(self):
        return self.name


class Post(models.Model):

    objects = PostManager()

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        help_text='Author of the post'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time the post was created'
    )
    updated = models.DateTimeField(
        auto_now=True,
        help_text='Date and time the post was last updated',
    )
    publish_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text='(optional) If set, when to publish the post'
    )
    title = models.CharField(
        max_length=255,
        help_text='Title of the post'
    )
    slug = models.SlugField(
        help_text='Slug of the post',
        db_index=True,
        unique=True,
        null=True,
        blank=True,
    )
    content = models.TextField(
        help_text='Content of the post'
    )
    tags = models.ManyToManyField(
        Tag,
        help_text='Tags'
    )

    def __str__(self):
        return self.title
