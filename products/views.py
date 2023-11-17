from rest_framework import viewsets, permissions
from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Product model.

    This ViewSet provides the CRUD operations for the Product model.
    It uses the ProductSerializer for serialization and deserialization of Product instances.
    It uses the IsAuthenticated permission class to ensure that only authenticated users can access the API endpoints.
    """
    queryset = Product.objects.all()  # The queryset that should be used for list views, and that should be used as the base for lookups of individual instances.
    permission_classes = [
        permissions.IsAuthenticated  # The list of permission classes that should be used for this ViewSet.
    ]
    serializer_class = ProductSerializer  # The serializer class that should be used for this ViewSet.
