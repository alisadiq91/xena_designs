from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Review(models.Model):
    """
    Model to define the fields required to be displayed in reviews.
    """
    title = models.CharField(max_length=200)
    comments = models.TextField()
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
