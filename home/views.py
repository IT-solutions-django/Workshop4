from django.shortcuts import render
from django.views import View 
from contacts.models import (
    Quote, 
    Review, 
    Partner
)


class HomeView(View): 
    template_name = 'home/home.html' 

    def get(self, request): 
        quotes = Quote.objects.all()
        reviews = Review.objects.all()
        partners = Partner.objects.all()
        context = {
            'is_home_page': True,
            'quotes': quotes,
            'reviews': reviews,
            'partners': partners,
        }
        return render(request, self.template_name, context) 
    

