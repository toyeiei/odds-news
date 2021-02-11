from django.shortcuts import render
from django.http import HttpResponse
from news.models import News
from django.views import View

# Create your views here.
# function vs. class based views

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