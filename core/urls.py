import debug_toolbar
from django.contrib import admin
from django.urls import path, include
# to get images to render that have been uploaded from admin page.
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('acrotrainer.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)