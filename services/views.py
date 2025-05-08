from django.shortcuts import render
from django.views import View 
from .models import Service
from blog.models import Article, ArticleCategory


class ServicesView(View): 
    template_name = 'services/services.html' 

    def get(self, request): 
        services = Service.objects.all()
        context = {
            'services': services, 
        }
        return render(request, self.template_name, context)
    

class ServiceDetailView(View):
    template_name = 'services/service_detail.html'

    def get(self, request, slug: str):
        service = Service.objects.get(slug=slug)

        articles = Article.objects.filter(services=service)
        categories = ArticleCategory.objects.filter(articles__in=articles).distinct()
        

        context = {
            'service': service,
            'articles': articles, 
            'categories': categories
        }
        return render(request, self.template_name, context)

