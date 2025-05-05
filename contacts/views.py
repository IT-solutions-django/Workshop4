from django.shortcuts import render
from django.views import View 
from .models import (
    Review, 
    Partner,
    Worker,
    Request,
)
from django.http import JsonResponse


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


class SaveRequestView(View):
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Request.objects.create(name=name, phone=phone, message=message)
        return JsonResponse({'success': True})
