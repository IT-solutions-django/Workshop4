from django.shortcuts import render, get_object_or_404
from django.views import View 
from .models import Article, ArticleCategory


class BlogView(View): 
    template_name = 'blog/blog.html' 

    def get(self, request): 
        articles = Article.objects.all()
        categories = ArticleCategory.objects.all()
        context = {
            'articles': articles,
            'categories': categories
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