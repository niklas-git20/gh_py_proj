from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^apartments/$', views.ApartListView.as_view(), name='aparts'),
    url(r'^apartments/(?P<pk>\d+)$', views.ApartDetailView.as_view(), name='apart-detail'),
    url(r'^owners/$', views.OwnerListView.as_view(), name='owners'),
    url(r'^owners/(?P<pk>\d+)$', views.OwnerDetailView.as_view(), name='owner-detail'),
    url(r'^reports/$', views.reports, name='reports'),   

]
urlpatterns += [    
    url(r'^service_form/$', views.ServiceView.as_view(), name='service_form'),
    url(r'^service/$', views.ServiceListView.as_view(), name='service'),
]

urlpatterns += [    
     url(r'^accrual_form/$', views.AccrualView.as_view(), name='accrual_form'),
     url(r'^accrual/$', views.AccrualListView.as_view(), name='accrual'),
]