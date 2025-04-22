from django.shortcuts import render
from django.views import View 


class ServicesView(View): 
    template_name = 'services/services.html' 

    def get(self, request): 
        context = {

        }
        return render(request, self.template_name, context)