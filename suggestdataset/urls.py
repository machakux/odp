"""suggestdataset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from . import views


urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^captcha/', include('captcha.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^', include('datasets.urls')),
    url(r'^feedback/', include('mrejesho.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^utawala/', admin.site.urls),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = getattr(settings, 'ADMIN_SITE_HEADER', '')
admin.site.index_title = getattr(settings, 'ADMIN_INDEX_TITLE', '')
admin.site.site_title = getattr(settings, 'SITE_NAME', '')
