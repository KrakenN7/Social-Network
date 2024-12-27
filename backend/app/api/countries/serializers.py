from rest_framework.serializers import ModelSerializer

from api.countries.models import Countries


class CountriesSerializer(ModelSerializer):
    class Meta:
        model = Countries
        fields = "__all__"
    