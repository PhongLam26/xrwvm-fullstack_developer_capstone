from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from djangoapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("djangoapp/", include("djangoapp.urls")),
    path("about", TemplateView.as_view(template_name="About.html"), name="about"),
    path("contact", TemplateView.as_view(template_name="Contact.html"), name="contact"),
    path("", views.frontend, name="home"),
    re_path(
        r"^(?:dealers|dealer/\d+|postreview/\d+|login|register)/?$",
        views.frontend,
        name="frontend-route",
    ),
]

urlpatterns += staticfiles_urlpatterns()
