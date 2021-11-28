from django import forms
from django.contrib.auth import get_user_model
from company.models import Company


User = get_user_model()


class CompanyCreationForm(forms.Form):
    """
    Form for creating a new company
    """
    name = forms.CharField(label='Company Name', max_length=100)
    description = forms.CharField(label='Company Description', max_length=100)
    email = forms.EmailField(label='Company Email', max_length=100)
    phone = forms.CharField(label='Company Phone', max_length=100)
    address = forms.CharField(label='Company Address', max_length=100)
    city = forms.CharField(label='Company City', max_length=100)
    website = forms.URLField(label='Company Website', max_length=100)
    logo = forms.ImageField(label='Company Logo', max_length=100)

    class Meta:
        model = Company
        fields = ("name", "description", "city", "address",
                  "phone", "email", "website", "logo",)
