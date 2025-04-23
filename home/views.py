from django.shortcuts import render
from django.views import View 


class HomeView(View): 
    template_name = 'home/home.html' 

    def get(self, request): 
        context = {
            'is_home_page': True,
        }
        return render(request, self.template_name, context) 
    

