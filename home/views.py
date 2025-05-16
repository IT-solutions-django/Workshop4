from django.shortcuts import render
from django.views import View 
from contacts.models import (
    Quote, 
    Review, 
    Partner
)
from blog.models import Article, ArticleCategory
from collections import defaultdict
from django.utils.html import strip_tags


class HomeView(View): 
    template_name = 'home/home.html' 

    def get(self, request): 
        quotes = Quote.objects.all()
        reviews = Review.objects.all()
        partners = Partner.objects.all()
        categories = ArticleCategory.objects.all()
        articles = Article.objects.all()

        region_dict = defaultdict(lambda: {'projects': []}) 
        for article in articles:
            if not article.region_code:
                continue

            region_data = region_dict[article.region_code]['projects']

            region_data.append({
                'image': article.image.url if article.image else '',
                'title': article.name,
                'subtitle': article.subtitle,
                'info': f"{self._get_area(article)} | {article.created_at.year} г. | {self._get_city(article)}",
                'category': article.category.name if article.category else None,
            })

        active_regions = list(region_dict.keys())

        context = {
            'is_home_page': True,
            'quotes': quotes,
            'reviews': reviews,
            'partners': partners,
            'categories': categories,
            'articles': articles,

            'my_variable': region_dict, 
            'active_regions': active_regions
        }
        return render(request, self.template_name, context) 
    
    def _get_area(self, article):
        # Заглушка, можно вытянуть из article.content или добавить поле area
        return "20 тыс м2"

    def _get_city(self, article):
        # Аналогично: можно вытащить из content, subtitle или добавить отдельное поле
        return "Город"
    

class Home1View(View):
    template_name = 'home/home1.html'

    def get(self, request): 
        quotes = Quote.objects.all()
        reviews = Review.objects.all()
        partners = Partner.objects.all()
        categories = ArticleCategory.objects.all()
        articles = Article.objects.all()
        context = {
            'is_home_page': True,
            'quotes': quotes,
            'reviews': reviews,
            'partners': partners,
            'categories': categories,
            'articles': articles,
        }
        return render(request, self.template_name, context) 


class Home2View(View):
    template_name = 'home/home2.html'

    def get(self, request): 
        quotes = Quote.objects.all()
        reviews = Review.objects.all()
        partners = Partner.objects.all()
        categories = ArticleCategory.objects.all()
        articles = Article.objects.all()
        context = {
            'is_home_page': True,
            'quotes': quotes,
            'reviews': reviews,
            'partners': partners,
            'categories': categories,
            'articles': articles,
        }
        return render(request, self.template_name, context)


class Home3View(View):
    template_name = 'home/home3.html'

    def get(self, request): 
        quotes = Quote.objects.all()
        reviews = Review.objects.all()
        partners = Partner.objects.all()
        categories = ArticleCategory.objects.all()
        articles = Article.objects.all()
        context = {
            'is_home_page': True,
            'quotes': quotes,
            'reviews': reviews,
            'partners': partners,
            'categories': categories,
            'articles': articles,
        }
        return render(request, self.template_name, context)


