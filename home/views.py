from django.shortcuts import render
from django.views import View 
from contacts.models import Quote, Review


class HomeView(View): 
    template_name = 'home/home.html' 

    def get(self, request): 
        quotes = Quote.objects.all()
        reviews = Review.objects.all()
        context = {
            'is_home_page': True,
            'quotes': quotes,
            'reviews': reviews,
        }
        return render(request, self.template_name, context) 
    

