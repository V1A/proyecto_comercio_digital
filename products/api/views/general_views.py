from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser

from base.api import GeneralListApiView
from products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    parser_classes = (JSONParser, MultiPartParser, )

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    parser_classes = (JSONParser, MultiPartParser, )
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
