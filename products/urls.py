from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ProductViewSet
from rest_framework.permissions import AllowAny

# Create a router for the ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

# Create a schema view for the Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="Product API",  # The title of the API
        default_version='v1',  # The default version of the API
        description="API documentation for the Product app",  # A brief description of the API
    ),
    public=True,  # The API is public and does not require authentication
    permission_classes=(AllowAny,),  # Allow any user to access the Swagger UI
    authentication_classes=(),  # No authentication is required to access the Swagger UI
)

# Define the URL patterns for the API
urlpatterns = [
                  # JSON and YAML formats of the API schema, without the Swagger UI
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  # The Swagger UI for the API schema
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  # The ReDoc UI for the API schema
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  # The URL patterns for the ProductViewSet
              ] + router.urls
