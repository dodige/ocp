from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class Info_membres(models.Model):
    numero = models.IntegerField(unique=True)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    adresse = models.CharField(max_length= 100)
    telephone = models.CharField(max_length=15)
    courriel = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    nombre_enfants = models.IntegerField(default=0)
    etat_civil = models.CharField(max_length=50)
    prenom_conjoint = models.CharField(max_length=50)
    nom_conjoint = models.CharField(max_length=50)

class ref_Statut_membre(models.Model):
     code = models.IntegerField(unique=True,default=1)
     description = models.CharField(max_length= 50)

class ref_Staff(models.Model):
     prenom = models.CharField(max_length=50)
     nom = models.CharField(max_length=50)
     poste = models.CharField(max_length=50)

class ref_liste_de_cours(models.Model):
     code = models.IntegerField(unique=True, default=1)
     description = models.CharField(max_length=50)

class ref_type_de_transaction(models.Model):
     code = models.IntegerField(unique=True, default=1)
     description = models.CharField(max_length=50)

class ref_type_de_suivi(models.Model):
     code = models.IntegerField(unique=True, default=1)
     description = models.CharField(max_length=50)

class cours_complete(models.Model):
     numero = models.ForeignKey(Info_membres, on_delete=models.CASCADE)
     code = models.ForeignKey(ref_liste_de_cours, on_delete=models.CASCADE)
     modified_by = models.ForeignKey(ref_Staff, on_delete=None)

class info_suivi(models.Model):
     numero = models.ForeignKey(Info_membres, on_delete=models.CASCADE)
     suivi_detail = models.CharField(max_length=150)
     date = models.DateTimeField('date de modification')
     modified_by = models.ForeignKey(ref_Staff, on_delete=None)

class transaction_financiere
     numero =  models.ForeignKey(Info_membres, on_delete=models.CASCADE)
     transaction = models.ForeignKey(ref_type_de_transaction, on_delete=None)
     montant = models.IntegerField()
     modified_by = models.ForeignKey(ref_Staff, on_delete=None)