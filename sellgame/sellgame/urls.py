from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news import views
from sellgame import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('catalog/', include('catalog.urls', namespace='shop')),
    path('account/', include('account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)