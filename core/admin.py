from django.contrib import admin
from .models import Ocupacion, Persona, Episodio

from django.contrib import admin
from .models import Persona, Ocupacion, Episodio

# Personalización del admin para Persona
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'verificado', 'avatar', 'linkedin', 'whatsapp')  
    search_fields = ('nombre',)  
    list_filter = ('ocupacion', 'verificado')  
    list_per_page = 5  

# Personalización del admin para Ocupacion
class OcupacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  
    search_fields = ('nombre',)  
    list_per_page = 5  

# Personalización del admin para Episodio
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracion', 'numero', 'descripcion', 'anfitrion', 'suscriptores', 'likes', 'comentarios', 'descargas')
    search_fields = ('titulo',)  
    list_filter = ('anfitrion', 'numero') 
    list_per_page = 5  

# Registrar los modelos en el panel de administración
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Ocupacion, OcupacionAdmin)
admin.site.register(Episodio, EpisodioAdmin)
