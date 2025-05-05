from django.shortcuts import render
from django.views import View 
from .models import Service


class ServicesView(View): 
    template_name = 'services/services.html' 

    def get(self, request): 
        services = Service.objects.all()
        context = {
            'services': services
        }
        return render(request, self.template_name, context)