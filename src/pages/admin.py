from django.contrib import admin

from .models import Page, PageSection, PageSlide
from staff.models import Person
from app.utils import user_is_group_member

# Register your models here.
class PageSectionInline(admin.StackedInline):
    model = PageSection
    extra = 0

    # class Media:
    #     js = ('tinymce/tinymce.min.js',
    #           'tinymce/init.js', )

class PageSlideInLine(admin.StackedInline):
    model = PageSlide
    extra = 1

class PageAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'slug', 'template', 'parent', 'url', 'created_at', 'updated_at', )
    readonly_fields = ('url', 'created_at', 'updated_at', 'author', )
    list_display = ('title', 'url', 'updated_at',)
    prepopulated_fields = {'slug': ('title', )}

    inlines = (PageSlideInLine, PageSectionInline, )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        elif user_is_group_member(request.user, 'Редактор сайта'):
            return qs

        elif user_is_group_member(request.user, 'Сотрудник'):
            person = Person.objects.get(user=request.user)
            return qs.filter(author=person)

        else:
            return qs.none()

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.readonly_fields = ('created_at', 'updated_at', 'url', )

        elif user_is_group_member(request.user, 'Редактор сайта'):
            self.readonly_fields = ('created_at', 'updated_at', 'url', )

        elif user_is_group_member(request.user, 'Сотрудник'):
            self.readonly_fields = ('created_at', 'updated_at', 'author', 'url')
        else:
            self.readonly_fields = self.fields

        return super(PageAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'author'):
            obj.author = request.user.person

        obj.slug = obj.slug.lower()

        if obj.parent:
            obj.url = obj.parent.url + '/' + obj.slug
        else:
            obj.url = obj.slug

        obj.save()

    class Media:
        js = ('tinymce/tinymce.min.js',
              'tinymce/init.js', )

admin.site.register(Page, PageAdmin)

