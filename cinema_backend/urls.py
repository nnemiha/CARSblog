# cinema_backend/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import vue_app
from django.views.generic.base import RedirectView
from django.templatetags.static import static as static_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('favicon.ico', RedirectView.as_view(url=static_static('favicon.ico'), permanent=True)),
    path('', vue_app),
    # Исключаем media и static из SPA catch-all, чтобы картинки и статика отдавались корректно
    re_path(r'^(?!api/|admin/|media/|static/).*$' , vue_app),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
