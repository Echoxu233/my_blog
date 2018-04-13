from django.db import models

# Create your models here.
class Comment(models.Model):
    Comment = models.CharField(max_length=180, null=True, blank=True)
    user = models.CharField(max_length=180, null=True, blank=True)


    def __str__(self):
        return self.Comment