from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from Payment.views import PaymentViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = SimpleRouter()
router.register('cancel-pay', PaymentViewSet)



schema_view = get_schema_view(
   openapi.Info(
      title="AVN Machine",
      default_version= 'Pochta',
      description="Burda senin icin her sey var",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MY liCENSE"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

 #SWAGGER
    path(r'', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('admin/', admin.site.urls),
    path('', include('Payment.urls')),
    path('', include(router.urls))
]
