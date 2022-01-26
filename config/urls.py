from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

from estagio.main.views import (
    BlogListView,
    BlogDetailView,
    blog_category,
    ContactFormView,
    ProjectListView,
    ProjectDetailView,
    gera_pdf_view,
)

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("cadastro_escola/", TemplateView.as_view(template_name="pages/cadastro_escola.html"), name="cadastro_escola"),
    path("documentos/", TemplateView.as_view(template_name="pages/documentos.html"), name="documentos"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("estagio.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("estagio/<slug:slug>/", BlogDetailView.as_view(), name="blog-detail"),
    path("estagio/category/<slug:category>/", blog_category, name='categories'),
    path("portfolio/", ProjectListView.as_view(), name="portfolio"),
    path("portfolio/<slug:slug>", ProjectDetailView.as_view(), name="project-details"),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("gera_pdf", gera_pdf_view.as_view(), name="gera_pdf"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
