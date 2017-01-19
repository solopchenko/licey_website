from django.contrib import admin
from .models import EduLevel, EduProgram, EduCourse

# Register your models here.

class EduProgramInline(admin.StackedInline):
    model = EduProgram

class EduLevelAdmin(admin.ModelAdmin):
    inlines = (EduProgramInline, )

class EduProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'form', )
    filter = ('form', )

class EduCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )

admin.site.register(EduLevel, EduLevelAdmin)
admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EduCourse, EduCourseAdmin)