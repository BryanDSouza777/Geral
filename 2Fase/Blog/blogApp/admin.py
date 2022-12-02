from django.contrib import admin
from .models import Animes, TipoHardware, Hardware, Jogos
# Register your models here.
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('nome','episodios','temporadas','lançamento','mostrar','foto')
    list_display_links = ('nome',)
    list_per_page = 6
    search_fields = ('nome',)
    list_editable = ('episodios','temporadas','lançamento','mostrar','foto')

class HardwareAdmin(admin.ModelAdmin):
    list_display = ('nome','marca','peça','lançamento','mostrar','foto')
    list_display_links = ('nome',)
    list_per_page = 6
    search_fields = ('nome','peça','marca')
    list_editable = ('marca','peça','lançamento','mostrar','foto')

class JogosAdmin(admin.ModelAdmin):
    list_display = ('nome','desenvolvedora','lançamento','mostrar','foto')
    list_display_links = ('nome','desenvolvedora')
    list_per_page = 6
    search_fields = ('nome',)
    list_editable = ('lançamento','mostrar','foto')

admin.site.register(Animes, AnimeAdmin)
admin.site.register(TipoHardware)
admin.site.register(Hardware, HardwareAdmin)
admin.site.register(Jogos, JogosAdmin)