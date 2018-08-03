# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import ref_liste_de_cours
from .models import ref_Statut_membre
from .models import ref_Staff
from .models import ref_type_de_suivi
from .models import ref_type_de_transaction
from .models import Info_membres
from .models import cours_complete
from .models import info_suivi
from .models import transaction_financiere



class Info_membresViewAdmin(admin.ModelAdmin):
    list_display = ['numero_de_membre', 'nom', 'prenom']


class info_suiviAdmin(admin.ModelAdmin):
    list_display = ['numero_de_membre', 'suivi_detail']



# Register your models here.
admin.site.register(Info_membres, Info_membresViewAdmin)
admin.site.register(cours_complete)
admin.site.register(info_suivi, info_suiviAdmin)
admin.site.register(transaction_financiere)
admin.site.register(ref_liste_de_cours)
admin.site.register(ref_type_de_suivi)
admin.site.register(ref_Staff)
admin.site.register(ref_Statut_membre)
admin.site.register(ref_type_de_transaction)





