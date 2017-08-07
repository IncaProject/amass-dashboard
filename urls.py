from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import include, url

from nine import versions

admin.autodiscover()

urlpatterns = []
url_patterns_args = [
    # django-dash URLs:
    url(r'^dashboard/', include('dash.urls')),



    # django-dash RSS contrib plugin URLs:
    url(r'^dash/contrib/plugins/rss-feed/',
        include('dash.contrib.plugins.rss_feed.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^administration/', include(admin.site.urls)),

    # django-registration URLs:
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', TemplateView.as_view(template_name='home.html')),

    # django-dash public dashboards contrib app:
    url(r'^', include('dash.contrib.apps.public_dashboard.urls')),

]

if versions.DJANGO_LTE_1_7:
    urlpatterns += i18n_patterns('', *url_patterns_args)
else:
    urlpatterns += i18n_patterns(*url_patterns_args)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
