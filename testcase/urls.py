from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
from testcase import settings
from django.conf.urls.static import static
from .views import home
from bookmarks.views import parsing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='main_page'),
    path('accounts/', include('app_accounts.urls')),
    path('add/', parsing, name='parse_page'),
]


urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)