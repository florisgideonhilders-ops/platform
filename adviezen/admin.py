from django.contrib import admin

from .models import SearchQuery, Zaak


@admin.register(Zaak)
class ZaakAdmin(admin.ModelAdmin):
    list_display = ('octopus_zaaknummer', 'onderwerp', 'dictum', 'aangemaakt_op')
    search_fields = ('octopus_zaaknummer', 'onderwerp', 'advies_tekst', 'dictum')
    list_filter = ('onderwerp', 'dictum')


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('gebruiker', 'zoekterm', 'onderwerp_filter', 'dictum_filter', 'resultaten_telling', 'aangemaakt_op')
    search_fields = ('gebruiker__username', 'zoekterm')
    list_filter = ('onderwerp_filter', 'dictum_filter')
