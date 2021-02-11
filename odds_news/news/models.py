from django.db import models

# Create your models here.
# ORM
class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

    def __str__(self):
        return self.title