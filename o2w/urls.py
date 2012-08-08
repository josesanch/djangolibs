from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/translation/', include('rosetta.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^(?P<slug>.*)/$', 'eurolevantedesarrollos.views.content', name='node'),
)


# Static
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
