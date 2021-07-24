from django.contrib import admin
from .models import bridal
from django.utils.html import format_html

# Register your models here.
class bridalAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius: 40px;"/>'.format(object.photo.url))
    thumbnail.short_description ='image'
    list_display= ('id', 'thumbnail','type',  'design', 'purpose', 'aouther_name', 'service_place')
    list_display_links =('id', 'thumbnail', 'type', 'design', 'aouther_name',)
    search_fields = ('sub_title', 'type', 'aouther_name',)
   # list_editable = ('is_feature',)
   # list_filter = ('car_title','city', 'model',)
admin.site.register(bridal,bridalAdmin)