# -*- coding: utf-8 -*-


from django.db import models
from django.forms import ModelForm

# Create your models here.

import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class ref_Statut_membre(models.Model):
     code = models.IntegerField(unique=True,default=1)
     description = models.CharField(max_length= 50)

     def __str__(self):
         return self.description + '('+str(self.code) + ')'



class Info_membres(models.Model):

    ##    ('Membre', 'Membre'),
    #    ('NouveauConverti', 'Nouveau Converti'),
    #    ('Visiteur', 'Visiteurs'),
    #    ('Ouvrier', 'Ouvrier'),
    #    ('Autres','Autre'),
    #)

    numero_de_membre = models.IntegerField(unique=True)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    adresse = models.CharField(max_length= 100)
    telephone = models.CharField(max_length=15)
    courriel = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    nombre_enfants = models.IntegerField(default=0)
    etat_civil = models.CharField(max_length=50)
    prenom_conjoint = models.CharField(max_length=50)
    nom_conjoint = models.CharField(max_length=50)
    #statut = models.CharField(choices=STATUT_DE_MEMEBRE,default='Membre',)
    statut = models.ForeignKey(ref_Statut_membre, on_delete=None)
    information_sur_eglise_precedente = models.TextField(max_length=200)
    a_suivi_cours_la_foi_transforme = models.BooleanField(default=False)
    a_suivi_cours_de_predication = models.BooleanField(default=False)
    a_suivi_cours_de_membre = models.BooleanField(default=False)
    a_suivi_cours_de_ouvrier = models.BooleanField(default=False)

    def __str__(self):
        return   self.prenom + ' ' + self.nom  + ' ('  + str(self.numero_de_membre)+ ')'



class MembreForm(ModelForm):
    class Meta:
        model = Info_membres
        fields = '__all__'

class ref_Staff(models.Model):
     prenom = models.CharField(max_length=50)
     nom = models.CharField(max_length=50)
     poste = models.CharField(max_length=50)

     def __str__(self):
         return self.prenom + ' ' + self.nom + '('+self.poste +')'

class ref_liste_de_cours(models.Model):
     code = models.IntegerField(unique=True, default=1)
     description = models.TextField(max_length=50)

     def __str__(self):
         return self.description + ' (' +str(self.code) + ')'

class ref_type_de_transaction(models.Model):
     code = models.IntegerField(unique=True, default=1)
     description = models.TextField(max_length=50)

     def __str__(self):
         return self.description + ' (' + str(self.code)+ ')'

class ref_type_de_suivi(models.Model):
     code = models.IntegerField(unique=True, default=1)
     description = models.CharField(max_length=50)

     def __str__(self):
         return self.description + ' (' + str(self.code) + ')'

class cours_complete(models.Model):
     numero_de_membre = models.ForeignKey(Info_membres, on_delete=models.CASCADE)
     code = models.ForeignKey(ref_liste_de_cours, on_delete=models.CASCADE)
     modified_by = models.ForeignKey(ref_Staff, on_delete=None)

class info_suivi(models.Model):
     numero_de_membre = models.ForeignKey(Info_membres, on_delete=models.CASCADE)
     suivi_detail = models.TextField(max_length=150)
     date = models.DateTimeField('date de modification')
     modified_by = models.ForeignKey(ref_Staff, on_delete=None)

class transaction_financiere(models.Model):
     numero_de_membre =  models.ForeignKey(Info_membres, on_delete=models.CASCADE)
     transaction = models.ForeignKey(ref_type_de_transaction, on_delete=None)
     montant = models.IntegerField()
     date = models.DateTimeField('date de modification',blank=True, null=True)
     modified_by = models.ForeignKey(ref_Staff, on_delete=None)

     def __str__(self):
         return  self.numero_de_membre.prenom + " " + self.numero_de_membre.nom + "  " + self.transaction.description + ": " +str(self.montant) +"$" + " date: " + str(self.date)




class transaction_form(ModelForm):
    class Meta:
        model = transaction_financiere
        fields = ['numero_de_membre', 'transaction','montant','modified_by']



class info_suivi_form(ModelForm):
    #def __init__(self, *args, **kwargs):
     #  super(info_suivi_form, self).__init__(*args, **kwargs)
      # self.fields['numero_de_membre'].widget.attrs['readonly'] = True

    class Meta:
        model = info_suivi
        fields = ['numero_de_membre', 'suivi_detail', 'date', 'modified_by']
