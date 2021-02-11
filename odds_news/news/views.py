from django.shortcuts import render
from django.http import HttpResponse
from news.models import News
from django.views import View
import json

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import News 
from .serializers import NewsSerializer

# Create your views here.
# function vs. class based views

class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsAPISimpleView(APIView):
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
        
        return Response(data)

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