from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .serializers import *
from .paginations import ProductPagination


class CollectionListView(ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryListView(ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class MetalListView(ListCreateAPIView):
    queryset = Metal.objects.all()
    serializer_class = MetalSerializer

class MaterialListView(ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class ColorListView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class StoneListView(ListCreateAPIView):
    queryset = Stone.objects.all()
    serializer_class = StoneSerializer

class ThemeListView(ListCreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    @list_route()
    def filter(self, request):
        products = getQuery(request)
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)



# Helper Function
def processUrlParam(paramList, groupModel):
    valueList = []
    for param in paramList:
        try:
            g = groupModel.objects.get(key=param)
        except:
            continue
        else:
            valueList.append(g.value)
    return valueList

def getQuery(request):
    minprice = request.GET.get('minp', '0')
    maxprice = request.GET.get('maxp', '10000')
    collection = processUrlParam(request.GET.getlist('col'), Collection)
    category = processUrlParam(request.GET.getlist('cat'), Category)
    subcategory = processUrlParam(request.GET.getlist('subcat'), SubCategory)
    metal = processUrlParam(request.GET.getlist('metal'), Metal)
    material = processUrlParam(request.GET.getlist('material'), Material)
    color = processUrlParam(request.GET.getlist('color'), Color)
    stone = processUrlParam(request.GET.getlist('stone'), Stone)
    theme = processUrlParam(request.GET.getlist('theme'), Theme)
    newest = request.GET.get('new', '')
    products = Product.objects.filter(
        price__gte=minprice,
        price__lte=maxprice,
    )

    if collection:
        products_collection = Product.objects.none()
        for col in collection:
            products_collection = products_collection | products.filter(collection=col)
        products = products_collection
    if category:
        products_category = Product.objects.none()
        for cat in category:
            products_category = products_category | products.filter(category=cat)
        products = products_category
    if subcategory:
        products_subcategory = Product.objects.none()
        for subcat in subcategory:
            products_subcategory = products_subcategory | products.filter(subcategory=subcat)
        products = products_subcategory

    if metal:
        products_metal = Product.objects.none()
        for me in metal:
            products_metal = products_metal | products.filter(metal=me)
        products = products_metal
    if material:
        products_material = Product.objects.none()
        for ma in material:
            products_material = products_material | products.filter(material=ma)
        products = products_material
    if color:
        products_color = Product.objects.none()
        for c in color:
            products_color = products_color | products.filter(color=c)
        products = products_color
    if stone:
        products_stone = Product.objects.none()
        for s in stone:
            products_stone = products_stone | products.filter(stone=s)
        products = products_stone
    if theme:
        products_theme = Product.objects.none()
        for t in theme:
            products_theme = products_theme | products.filter(theme=t)
        products = products_theme

    if newest:
        products = products.filter(newest=True)
    return products