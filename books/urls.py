from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/category/', GetAllCategory.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

