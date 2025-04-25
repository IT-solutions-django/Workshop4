from django.shortcuts import render
from django.views import View 
from .models import (
    Review, 
    Partner,
    Worker,
)


class AboutCompanyView(View): 
    template_name = 'contacts/company.html' 

    def get(self, request): 
        reviews = Review.objects.all()
        partners = Partner.objects.all()
        workers = Worker.objects.all()
        context = {
            'reviews': reviews,
            'partners': partners,
            'workers': workers,
        }
        return render(request, self.template_name, context)