from django.shortcuts import render
from company.forms import CompanyCreationForm


def company_view(request):
    context = {
        'company_creation_form': CompanyCreationForm(),
    }
    return render(request, 'company/company.html', context)
