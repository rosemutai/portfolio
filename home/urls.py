from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, projects, resume, contact
urlpatterns = [
    path('', home, name="home"),
    path('projects', projects, name="projects"),
    path('resume', resume, name="resume"),
    path('contactme', contact, name="contact")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    