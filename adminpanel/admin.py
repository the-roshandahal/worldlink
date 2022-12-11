from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
admin.site.site_header = "Admin panel"

from django_summernote.models import Attachment
class Description(SummernoteModelAdmin):
    summernote_fields = ('tour_details','itinerary')

class SliderFields(admin.ModelAdmin):
    list_display = ('main_text', 'order',)

admin.site.unregister(Attachment)
admin.site.register(Slider,SliderFields)
admin.site.register(TourCategory)
admin.site.register(Destination)
admin.site.register(Tour,Description)
admin.site.register(Blog)
admin.site.register(Testimonial)