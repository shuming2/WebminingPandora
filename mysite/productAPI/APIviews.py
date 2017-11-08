from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from .serializers import *
from .paginations import ProductPagination


class CollectionListView(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class SubCategoryListView(ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
#TODO: other group model API view


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
