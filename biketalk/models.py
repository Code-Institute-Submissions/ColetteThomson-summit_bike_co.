from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# status of post
STATUS = ((0, "Draft"), (1, "Published"))


class Article(models.Model):
    """ ERD model for class Article """
    # model fields
    article_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # delete all related records if author deleted
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    article_detail = models.TextField()
    article_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='article_likes',
                                   blank=True)

    # helper methods for class Article:
    class Meta:
        ordering = ['-created_on']

    # returns a string representation of an object
    def __str__(self):
        return self.article_name

    # returns total number of likes on a post
    def number_of_likes(self):
        return self.likes.count()


class Opinion(models.Model):
    """ ERD model for class Opinion """
    # model fields
    # delete all related records if author deleted
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='opinions')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # helper methods for class Opinion:
    # order posts based on created_on field
    class Meta:
        ordering = ['created_on']

    # returns a string representation of an object
    def __str__(self):
        return f"Opinion {self.body} by {self.name}"
