# core/forms.py
from django import forms
from .models import Persona, Ocupacion, Episodio

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'ocupacion', 'verificado', 'avatar', 'linkedin', 'whatsapp']
    
    # Asegúrate de que el campo ocupacion esté configurado correctamente
    ocupacion = forms.ModelMultipleChoiceField(queryset=Ocupacion.objects.all(), widget=forms.CheckboxSelectMultiple)

class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = ['titulo', 'duracion', 'numero', 'descripcion', 'anfitrion', 'suscriptores', 'likes', 'comentarios', 'descargas', 'imagen']
    
    # Personalización de los campos si se desea
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del episodio'}))
    duracion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Duración del episodio(minutos)'}))
    numero = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número del episodio'}))
    descripcion = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del episodio'}))
    anfitrion = forms.ModelChoiceField(queryset=Persona.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    suscriptores = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    likes = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    comentarios = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    descargas = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
