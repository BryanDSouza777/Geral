from django.contrib import admin
from .models import Animes, TipoHardware, Hardware, Jogos
# Register your models here.
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('nome','episodios','temporadas','lançamento','mostrar','foto')
    list_display_links = ('nome',)
    list_per_page = 15
    search_fields = ('nome',)
    list_editable = ('mostrar',)

class HardwareAdmin(admin.ModelAdmin):
    list_display = ('nome','marca','peça','mostrar','foto')
    list_display_links = ('nome',)
    list_per_page = 15
    search_fields = ('nome',)
    list_editable = ('mostrar',)

class JogosAdmin(admin.ModelAdmin):
    list_display = ('nome','desenvolvedora','lançamento','mostrar','foto')
    list_display_links = ('nome',)
    list_per_page = 15
    search_fields = ('nome',)
    list_editable = ('mostrar',)

admin.site.register(Animes, AnimeAdmin)
admin.site.register(TipoHardware)
admin.site.register(Hardware, HardwareAdmin)
admin.site.register(Jogos, JogosAdmin)