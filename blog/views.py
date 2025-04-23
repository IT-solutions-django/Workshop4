from django.shortcuts import render
from django.views import View 


class BlogView(View): 
    template_name = 'blog/blog.html' 

    def get(self, request): 
        context = {

        }
        return render(request, self.template_name, context)
    

class ArticleView(View): 
    template_name = 'blog/article.html' 

    def get(self, request): 
        context = {

        }
        return render(request, self.template_name, context)