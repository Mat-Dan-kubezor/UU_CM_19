from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Article


def article(request):
    articles = Article.objects.all().order_by('-created')
    items_per_page = request.GET.get('items_per_page', 5)
    paginator = Paginator(articles, items_per_page)
    page_number = request.GET.get('page')
    context = {
        'page_obj': paginator.get_page(page_number),
        'items_per_page': items_per_page
    }
    return render(request, 'article.html', context=context)
