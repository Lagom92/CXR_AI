from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import boards.views as boards_views
import accounts.views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boards.urls')),
    path('screening/', include('screening.urls')),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)