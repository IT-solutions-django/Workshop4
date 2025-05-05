from .models import CompanyInfo
from contacts.forms import RequestForm


def company_info(request):
    info = CompanyInfo.get_instance()

    context = {
        'company_info': info,
    }

    return context


def contact_form(request):
    return {
        'contact_form': RequestForm()
    }