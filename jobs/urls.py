from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.views.static import serve 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path('contact/', views.contact, name='contact'),
    path('mission/', views.mission, name='mission'),
    path('confidentialite/', views.confidentialite, name='confidentialite'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/<int:id>/', views.jobs_details, name='jobs-details'),
]