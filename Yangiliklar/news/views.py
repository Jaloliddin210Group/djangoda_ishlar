from django.shortcuts import render
#from django.http import HttpResponse

from .models import *
def index(request):
    news = News.objects.order_by('title')
    context={
                'news': news,
                'title': "Yangiliklar ro'yxati"
}
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }

    return render(request, template_name='news/category.html', context=context)







# news=News.objects.all()
# res = "<h1>Yangiliklar ro'hxati<h1>"
# for i in news:
#     res += f'<div>\n<p>{i.title}<p>\n<p>{i.content}<p>\n<div>\n<hr><br>'
#     return HttpResponse(res)


# def index(request):
#     print(request)
#     return HttpResponse("Hello world!!!")
# def name(request):
#     print(request)
#     return HttpResponse("<h1>Narzulloyev Jaloliddin <h1>")
# def index(request):
#     return  render(request, 'Yangiliklar news/index.html')

