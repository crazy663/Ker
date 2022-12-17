from django.urls import path

from djangoProject import settings
from . import views
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('<str:urlpath>', views.ContView.as_view(), name="Cont"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

