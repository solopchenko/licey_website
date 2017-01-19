from django.contrib import admin
from .models import Document, DocumentCategory

# Register your models here.
class DocumentInline(admin.TabularInline):
    model = Document
    readonly_fields = ('created_at', 'updated_at', )
    extra = 1

class DocumentCategoryAdmin(admin.ModelAdmin):
    inlines = (DocumentInline, )

admin.site.register(Document)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)