from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Apart, Owner, Service, Accrual
from .forms import ServiceForm, AccrualForm
from django.views import generic
#access for authenificated users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime




# Create your views here.
def index(request):
    """
    Display main page
    """
    # Main objects ammount generation
    num_aparts=Apart.objects.all().count()
    num_owners=Owner.objects.count()  # by default method 'all()' 

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html', context={'num_aparts':num_aparts,
                                'num_owners':num_owners,
                                'num_visits':num_visits}, # num_visits appended
    )



class ApartListView(generic.ListView):
    model = Apart
    #template_name = 'apart_list.html'
    paginate_by = 2


class ApartDetailView(LoginRequiredMixin, generic.DetailView):    
    model = Apart
    paginate_by = 2


class OwnerListView(generic.ListView):
    model = Owner
    #template_name = 'owner_list.html'
    paginate_by = 2


class OwnerDetailView(generic.DetailView):
    model = Owner
    paginate_by = 2


@login_required
def reports(request):
    # Display reports
    report = 'report 1'
    # Render the HTML report report.html
    return render(request,
        'reports.html', {"report": report}
    )



class ServiceListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing ordered service to current user.
    """
    model = Service
    template_name ='service_list.html'
    form_class = ServiceForm
    success_url = "/home/"
    paginate_by = 10

    def get_queryset(self):
        return Service.objects.filter(client=self.request.user).order_by('date_req')

class ServiceView(generic.CreateView):
    model = Service    
    template_name ='service_form.html'
    form_class = ServiceForm
    success_url = "/home/"


    
class AccrualListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing ordered service to current user.
    """
    model = Accrual
    template_name ='accrual_list.html'
    form_class = AccrualForm
    success_url = "/home/"
    paginate_by = 10

    def get_queryset(self):
        return Accrual.objects.filter(nbr=self.request.user).order_by('nbr')


class AccrualView(generic.CreateView):
    model = Accrual    
    template_name ='accrual_form.html'
    form_class = AccrualForm
    success_url = "/home/"





