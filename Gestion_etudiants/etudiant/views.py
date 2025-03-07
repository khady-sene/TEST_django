from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant
from .forms import EtudiantForm

# Afficher la liste des étudiants
def liste_etudiants(request):
    etudiants = Etudiant.objects.all().order_by('-created_at')  # Récupère tous les étudiants
    return render(request, 'etudiant/liste_etudiants.html', {'etudiants': etudiants})

# Page d'accueil
def index(request):
    return render(request, 'etudiant/index.html')

# À propos
def about(request):
    return render(request, 'etudiant/about.html')

# Ajouter un étudiant
def ajouter_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etudiants')  # Redirige vers la liste des étudiants après ajout
    else:
        form = EtudiantForm()

    return render(request, 'etudiant/ajouter.html', {'form': form})

# Modifier un étudiant
def modifier_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiants')  # Redirige vers la page liste des étudiants après modification
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'etudiant/modifier.html', {'form': form, 'etudiant': etudiant})

# Supprimer un étudiant
def supprimer_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    
    if request.method == "POST":
        etudiant.delete()
        return redirect('etudiants')  # Redirige vers la page liste des étudiants après suppression

    return render(request, 'etudiant/supprimer.html', {'etudiant': etudiant})
