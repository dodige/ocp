from django.contrib import admin

from .models import PageView
from .models import Info_membres
from .models import ref_liste_de_cours

# Register your models here.


class PageViewAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'timestamp']

admin.site.register(PageView, PageViewAdmin)
#admin.site.register(PageView, PageViewAdmin)


class Info_membresViewAdmin(admin.ModelAdmin):
    list_display = ['numero', 'nom', 'prenom']


admin.site.register(Info_membres, Info_membresViewAdmin)
