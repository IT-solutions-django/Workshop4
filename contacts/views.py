from django.shortcuts import render
from django.views import View 


class AboutCompanyView(View): 
    template_name = 'contacts/company.html' 

    def get(self, request): 
        context = {

        }
        return render(request, self.template_name, context)