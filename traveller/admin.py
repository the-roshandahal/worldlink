from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
admin.site.site_header = "Admin panel"

from django_summernote.models import Attachment
class CompanyField(SummernoteModelAdmin):
    summernote_fields = ('about_us_page_content')


class Description(SummernoteModelAdmin):
    summernote_fields = ('tour_details','itinerary')


class BlogField(SummernoteModelAdmin):
    summernote_fields = ('blog')
class SliderFields(admin.ModelAdmin):
    list_display = ('text_1', 'order',)
class BookingFields(admin.ModelAdmin):
    list_display= ('name', 'tour')


admin.site.unregister(Attachment)
admin.site.register(Slider,SliderFields)
admin.site.register(TourCategory)
admin.site.register(Destination)
admin.site.register(Tour,Description)
admin.site.register(Blog,BlogField)
admin.site.register(Testimonial)
admin.site.register(Partner)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Booking,BookingFields)
admin.site.register(CompanySetup,CompanyField)