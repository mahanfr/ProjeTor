from django.shortcuts import redirect, render
from company.forms import CompanyCreationForm
from company.models import Company, JoinRequest


def company_view(request):
    context = {
        'company_creation_form': CompanyCreationForm(),
    }
    return render(request, 'company/company.html', context)


def company_create(request):
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            print('valid')
            instance = form.save(commit=False)
            instance.admin = request.user
            instance.save()
        else:
            print(form.errors)
    return redirect('company-view')


def company_join(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('description')
        JoinRequest.objects.create(
            company=Company.objects.get(name=name), description=desc, user=request.user)
    return redirect('company-view')
