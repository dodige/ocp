from django.contrib.auth.models import User
import django_filters

from .models import MembreForm, Info_membres, info_suivi, info_suivi_form, transaction_financiere, transaction_form


class TxFilter(django_filters.FilterSet):
    class Meta:
        model = transaction_financiere
        fields = ['numero_de_membre', 'transaction', 'montant', 'date' , 'modified_by']

