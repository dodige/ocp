from sys import path

from django.conf.urls import url
#from django.conf.urls import views
#from . import views
from vtapp import views
from django_filters.views import FilterView

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'ajout/',views.ajout, name='ajout'),
    url(r'consulter/',views.consulter, name='consulter'),
    url(r'finances/',views.finances, name='finances'),
    url(r'get_name/', views.get_name, name='get_name'),
    url(r'get_suivi/', views.get_suivi, name='get_suivi'),
    url(r'^membres/(?P<pk>\d+)$', views.MembresDetailView.as_view(), name='membres-detail'),
    url(r'membres/', views.MembresListView.as_view(), name='membres'),
    url(r'transaction/', views.transaction, name='transaction'),
    url(r'transactionDetail/(?P<pk>\d+)$', views.transactionDetailView.as_view(), name='transactionDetail'),
    #url(r'^membres/(?P<pk>\d+)$', views.MembresDetailView.as_view(), name='membres-detail'),
    url(r'transactionList/', views.transactionListView.as_view(), name='membres'),
    url(r'^search/$', views.search, name='search'),

]

