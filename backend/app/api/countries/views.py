from rest_framework.generics import ListAPIView

from api.countries.models import Countries
from api.countries.serializers import CountriesSerializer


class CountriesListApiView(ListAPIView):
    pagination_class = None
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
