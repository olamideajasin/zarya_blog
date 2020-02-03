from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models (objects but stored in the database) here.

# class: this is used when defining an object (in this case, a post)
# Post: this is the name of the model!
# models.Model: identifying the object "Post" as a Django Model!
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Foreign Key is a link to another model
    title = models.CharField(max_length=200)
    # models.CharField is how you define text with a limited character count
    text = models.TextField()
    # models.TextField is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # The method "publish" below! def means that its a function/method.
    # def publish(self)= define the method "publish" for this object (Post)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    #When we call __str__(), we get a text string with the Post title.
    def __str__(self):
        return self.title