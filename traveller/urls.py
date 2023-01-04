from django.urls import path,include
from . import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path('destinations/', views.destinations, name="destinations"),
    path('tours/', views.tours, name="tours"),
    path('about_us/', views.about_us, name="about_us"),
    path('tour_single/<int:id>', views.tour_single, name="tour_single"),

    path('contact_us/', views.contact_us, name="contact_us"),
    path('blogs/', views.blogs, name="blogs"),
    path('blog_single/<int:id>', views.blog_single, name="blog_single"),


    path('book_trip/<int:id>', views.book_trip, name="book_trip"),

    path('destination_filter/<int:id>', views.destination_filter, name="destination_filter"),
    
    path('summernote/', include('django_summernote.urls')),

    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
