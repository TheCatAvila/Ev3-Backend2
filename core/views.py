from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

# Create your views here.
def index(request):
    personas = Persona.objects.all()
    episodios = Episodio.objects.all()
    return render(request, 'core/index.html', {'personas': personas, 'episodios': episodios})

# Vistas persona
def add_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('index')  
    else:
        form = PersonaForm()

    return render(request, 'core/personas/add_persona.html',  {'form': form})

def update_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    
    if request.method == 'POST':
        form = PersonaForm(request.POST, request.FILES, instance=persona)
        if form.is_valid():
            form.save()  
            return redirect('index') 
    else:
        form = PersonaForm(instance=persona) 

    return render(request, 'core/personas/update_persona.html', {'form': form})

def delete_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    persona.delete()
    return redirect('index')

# Vistas episodio
def add_episodio(request):
    if request.method == 'POST':
        form = EpisodioForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('index')  
    else:
        form = EpisodioForm()

    return render(request, 'core/episodios/add_episodio.html',  {'form': form})

def update_episodio(request, episodio_id):
    episodio = get_object_or_404(Episodio, id=episodio_id)
    
    if request.method == 'POST':
        form = EpisodioForm(request.POST, request.FILES, instance=episodio)
        if form.is_valid():
            form.save()  
            return redirect('index') 
    else:
        form = EpisodioForm(instance=episodio) 

    return render(request, 'core/episodios/update_episodio.html', {'form': form})

def delete_episodio(request, episodio_id):
    episodio = get_object_or_404(Episodio, id=episodio_id)
    episodio.delete()
    return redirect('index')