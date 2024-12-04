from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('add-persona/', add_persona, name="add_persona"),
    path('update-persona/<int:persona_id>/', update_persona, name='update_persona'),
    path('delete-persona/<int:persona_id>/', delete_persona, name='delete_persona'),
    path('add-episodio/', add_episodio, name="add_episodio"),
    path('update-episodio/<int:episodio_id>/', update_episodio, name='update_episodio'),
    path('delete-episodio/<int:episodio_id>/', delete_episodio, name='delete_episodio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)