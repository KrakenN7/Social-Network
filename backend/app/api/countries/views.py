from rest_framework.viewsets import ModelViewSet

from api.countries.models import Countries
from api.countries.serializers import CountriesSerializer


class CountriesViewSet(ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer

    def get_queryset(self):
        return self.queryset
