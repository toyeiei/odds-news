# from odds_news.categories.models import Category

from django.db import models
from categories.models import Category # impact db needs to migrate again

# Create your models here.
# ORM
class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()

    # key is the same name as model
    # one to many relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title