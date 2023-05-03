from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('', include('apps.store.urls')),
    path('', include(tf_urls)),
    path('', include('apps.users.urls')),
    path('admin/', admin.site.urls),
]


# Serve static and media files
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]

# admin.site.enable_nav_sidebar = False 
admin.site.site_header = "MFA Dashboard"
admin.site.site_title = "MFA Admin Portal"
# admin.site.index_title = "MFA | Dashboard"