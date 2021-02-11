from django.shortcuts import render
from django.http import HttpResponse
from news.models import News
from django.views import View
import json

# Create your views here.
# function vs. class based views

## API json
class NewsAPIView(View):
    def get(self, request):
        news = News.objects.all()

        data = []
        for each in news:
            item = {
                'title': each.title,
                'content': each.content,
                'category': each.category.name
            }
            data.append(item)

        return HttpResponse(
            # '[{"title": "Hello"}, {"title": "Today"}]', 
            # dump as string
            json.dumps(data),
            content_type='application/json'
        )

# extend django View
class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        # html = '<div>'
        # for each in news:
        #     html += '<div>'
        #     html += f'<h1>{each.title}</h1>'
        #     html += f'<p>{each.content}</p>'
        #     html += '</div>'
        # html += '</div>'
        # return HttpResponse(html)
        return render(
            request,
            'news.html',
            context = {
                'news': news
            }
        )

def news_view(request):
    if request.method == 'GET':
        news = News.objects.all()

        html = '<div>'
        
        for each in news:
            html += '<div>'
            html += f'<h1>{each.title}</h1>'
            html += f'<p>{each.content}</p>'
            html += '</div>'

        html += '</div>'
        return HttpResponse(html)