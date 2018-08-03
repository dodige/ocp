# -*- coding: utf-8 -*-


from django.shortcuts import render

from django.urls import reverse

from django.views import generic

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# Create your views here.

from .filters import TxFilter



from .models import MembreForm, Info_membres, info_suivi, info_suivi_form, transaction_financiere, transaction_form

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MembreForm(request.POST)  # type: object
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            #return HttpResponseRedirect('/vtapp/')
            return render(request, 'consulter.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MembreForm()

    return render(request, 'name.html', {'form': form})

def get_suivi(request):
    # if this is a POST request we need to process the form data
    mem2 = None

    membre = None
    suivi = info_suivi.objects.all()
    primarycle= request.GET.get('pk')
    membre = Info_membres.objects.get(pk=primarycle)

    if request.method == 'POST':
        #membre = Info_membres.objects.get(request.GET.get('pk'))
        # create a form instance and populate it with data from the request:
        form = info_suivi_form(request.POST)  # type: object
        #mem2 = (info_suivi)(info_suivi_form(request.POST)).numero_de_membre
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            #return HttpResponseRedirect('/vtapp/')
            #mem = form.__getattribute__('numero_de_membre')
            #return HttpResponseRedirect('/vtapp/membres/'+ mem.pk+'/')

            return render(request, 'info_membres_detail.html/', {'form': form, 'object': membre, 'suivi_list' : suivi})
    # if a GET (or any other method) we'll create a blank form
    else:
        mem2 = None
        info_suivi(numero_de_membre_id=primarycle)
        form = info_suivi_form(info_suivi(numero_de_membre=membre))
        #membre = Info_membres.objects.get(request.GET.get('pk'))



    return render(request, 'info_membres_detail.html', {'form': form , 'object': membre, 'suivi_list' : suivi})

def index(request):
    #return HttpResponse("VT Demo Application")
    return render(request, 'index.html')

def ajout(request):
    return render(request, 'ajout.html')


def consulter(request):

    if request.method == 'POST':
        form = MembreForm(request.POST)  # type: object
    else:
        form = MembreForm()

    return render(request, 'consulter.html', {'form': form})


def transaction(request):
    if request.method == 'POST':
        #membre = Info_membres.objects.get(request.GET.get('pk'))
        # create a form instance and populate it with data from the request:
        form =  transaction_form(request.POST)  # type: object
        #mem2 = (info_suivi)(info_suivi_form(request.POST)).numero_de_membre
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            #return HttpResponseRedirect('/vtapp/')
            #mem = form.__getattribute__('numero_de_membre')
            #return HttpResponseRedirect('/vtapp/membres/'+ mem.pk+'/')

            #return render(request, 'vtapp/info_membres_detail.html/', {'form': form, 'object': membre, 'suivi_list' : suivi})
            return render(request, 'post_form_tx.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        #mem2 = None
        #info_suivi(numero_de_membre_id=primarycle)
        form = transaction_form()
        #membre = Info_membres.objects.get(request.GET.get('pk'))

    #return render(request, 'vtapp/info_membres_detail.html', {'form': form , 'object': membre, 'suivi_list' : suivi})
    return render(request, 'transaction.html', {'form': form})





def finances(request):
    return render(request, 'finances.html')


    #suivi = info_suivi()




class transactionDetailView(generic.DetailView):
    model = transaction_financiere

    # suivi = info_suivi()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(transactionDetailView, self).get_context_data(**kwargs)
        # context = self().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['suivi_list'] = info_suivi.objects.all()
        #context['suivi_form'] = info_suivi_form(
        #    initial={"numero_de_membre": Info_membres.objects.get(pk=self.kwargs.get('pk'))})
        # info_suivi.objects.all()
        return context

    #def get_queryset(self):
     #   self.publisher = get_object_or_404(transaction_financiere, name=self.kwargs['publisher'])
     #   return Book.objects.filter(publisher=self.publisher)

class transactionListView(generic.ListView):
    model = transaction_financiere
    #paginate_by = 25

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', 'numero_de_membre')
        # validate ordering here
        return ordering


class MembresListView(generic.ListView):
    model = Info_membres

class MembresDetailView(generic.DetailView):
    model = Info_membres
    #suivi = info_suivi()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MembresDetailView,self).get_context_data(**kwargs)
        #context = self().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['suivi_list'] = info_suivi.objects.all()
        context['suivi_form'] = info_suivi_form(initial = {"numero_de_membre": Info_membres.objects.get(pk=self.kwargs.get('pk'))})
            #info_suivi.objects.all()
        return context

def search(request):
    tx_list =  transaction_financiere.objects.all()
    tx_filter = TxFilter(request.GET, queryset=tx_list)
    return render(request, 'tx_list.html', {'filter': tx_filter})