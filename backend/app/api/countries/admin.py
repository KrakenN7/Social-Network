from django.contrib import admin

from api.countries.models import Countries


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "alpha2",
        "alpha3",
        "region",
    ]
    list_filter = ["name"]
    list_editable = [
        "alpha2",
        "alpha3",
        "region",
    ]
    list_display_links = ["name"]
