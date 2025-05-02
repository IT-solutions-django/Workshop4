from django.shortcuts import render, get_object_or_404
from django.views import View 
from .models import Article, ArticleCategory
from home.services import get_paginated_collection


class BlogView(View): 
    template_name = 'blog/blog.html' 

    def get(self, request): 
        articles = Article.objects.all()
        categories = ArticleCategory.objects.all()

        articles = get_paginated_collection(request, articles)

        context = {
            'articles': articles,
            'categories': categories
        }
        return render(request, self.template_name, context)
    

class BlogCategoryView(View):
    template_name = 'blog/blog.html'

    def get(self, request, category_id: int):
        articles = Article.objects.filter(category_id=category_id)
        categories = ArticleCategory.objects.all()

        articles = get_paginated_collection(request, articles)

        context = {
            'articles': articles,
            'categories': categories, 
            'selected_category_id': category_id
        }
        return render(request, self.template_name, context)
    

class ArticleView(View): 
    template_name = 'blog/article.html' 

    def get(self, request, slug): 
        article = get_object_or_404(Article, slug=slug)
        context = {
            'article': article
        }
        return render(request, self.template_name, context)