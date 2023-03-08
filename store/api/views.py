from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import routers
from rest_framework.permissions import IsAdminUser
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'destroy', ):
            self.permission_classes = (IsAdminUser, )


