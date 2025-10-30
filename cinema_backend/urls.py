from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.templatetags.static import static as static_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('favicon.ico', RedirectView.as_view(url=static_static('favicon.ico'), permanent=True)),

    # Отдаём index.html для фронтенда (Vue SPA)
    re_path(r'^(?!api/|admin/|media/|static/|assets/).*$', 
            TemplateView.as_view(template_name='index.html')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
