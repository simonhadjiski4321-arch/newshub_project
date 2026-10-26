from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path(
        "",
        RedirectView.as_view(
            pattern_name="news:article_list",
            permanent=False,
        ),
        name="home",
    ),
    path("admin/", admin.site.urls),
    path("news/", include("news.urls")),
    path("comments/", include("comments.urls")),
    path("catalog/", include("catalog.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Serve uploaded media for the local exam server when DEBUG is disabled.
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]