from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# data model for blog posts


class Post(models.Model):
    """
    title = field for the post title (CharField which is VARCHAR column in the SQL database)
    slug = slug is a short label containing only letters, numbers, underscores or hyphens, used to create SEO-friendly
            URLs (SlugField which is VARCHAR column in the SQL database)
    author - User model attached as an author of the post. ForeignKey defines the relationship 'many to one' (each post
            is written by a user and one user can write many posts). on_delete defines a specific behaviour when the
            object is deleted: CASCADE means that if user is deleted also all related blog posts will be deleted.
            related_name allows us to access an opposite relation, User to Post, allowing us to use notation
            user.blog_posts
    body = stores the body of the post. (TextField which is TEXT column in the SQL database)
    __str__ method - allows setting up a human-readable representation of the object
    publish - storing date and time when the post was published (DateTimeField translates into DATETIME column
            in the SQL database)
    created - storing the date and time when the post was created (DateTimeField translates into DATETIME column
            in the SQL database)
    updated - storing the date and time when the post was last updated, updated automatically when saving the object
            (DateTimeField translates into DATETIME column in the SQL database)
    status - shows a status of a post and sets up a default status as draft (CharField which is VARCHAR column
            in the SQL database)
    """

    class Status(models.TextChoices):
        """
        Enumeration class defines a status of the post to allow saving a draft post before publication.
        DRAFT - not published, saved post
        PUBLISHED - published post
        """

        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        """
        Class defines metadata for the model.
        ordering - default order (reverse chronological order - from newest to oldest; descending order)
                when no order is specified in a query. Uses publish field to sort posts
        indexes - defines database indexes for the model, improving performance for filtering or ordering results
                by this filed
        """
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

