from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # custom ModelAdmin
    list_display = (
        'title',
        'content', # add comma at the end
    )