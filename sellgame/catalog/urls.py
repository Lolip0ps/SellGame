from django.urls import path
from catalog import views
from sellgame import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.catalog),
    path('post/<int:post_id>/', views.show_post, name='post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
