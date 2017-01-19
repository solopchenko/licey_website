from django.contrib import admin
from .models import Gallery, GalleryImage

# Register your models here.
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage

class GalleryAdmin(admin.ModelAdmin):
    inlines = (GalleryImageInline, )

admin.site.register(Gallery, GalleryAdmin)
