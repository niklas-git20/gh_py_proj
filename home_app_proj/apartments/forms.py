from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as ugt_lz
import datetime #for checking date range.
from .models import Service, Accrual


class DateInput(forms.DateInput):
    input_type = 'date'


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['prof_req', 'date_req', 'client']
        widgets = {
            'date_req': DateInput(),
        }


class AccrualForm(ModelForm):
    class Meta:
        model = Accrual
        fields = ['nbr', 'balance']
       

    



