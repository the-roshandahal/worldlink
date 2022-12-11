from django.urls import path,include
from . import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path('destinations/', views.destinations, name="destinations"),
    path('tours/', views.tours, name="tours"),
    path('tour_single/<int:id>', views.tour_single, name="tour_single"),
    path('summernote/', include('django_summernote.urls')),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
