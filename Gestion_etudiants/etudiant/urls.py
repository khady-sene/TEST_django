from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Page d'accueil
    path('about', views.about, name='about'),  # À propos
    
    # Afficher la liste des étudiants
    path('liste_etudiants/', views.liste_etudiants, name='liste_etudiants'),  
    
    # Ajouter un étudiant
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),  
    
    # Modifier un étudiant
    path('modifier/<int:etudiant_id>/', views.modifier_etudiant, name='modifier_etudiant'),  
    
    # Supprimer un étudiant
    path('supprimer/<int:etudiant_id>/', views.supprimer_etudiant, name='supprimer_etudiant'),
]
