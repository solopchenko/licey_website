from django.contrib import admin
from .models import NewsPage, NewsPageGalleryImage
from staff.models import Person
from app.utils import user_is_group_member
from django.conf import settings

# Register your models here.
class NewsPageGalleryImageInline(admin.StackedInline):
    model = NewsPageGalleryImage
    extra = 1

class NewsPageAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'announcement', 'content', 'published', 'published_at', 'created_at', 'updated_at', )
    readonly_fields = ('created_at', 'updated_at', 'author', )
    list_display = ('title', 'published', )
    inlines = (NewsPageGalleryImageInline, )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        elif user_is_group_member(request.user, 'Редактор новостей'):
            return qs

        elif user_is_group_member(request.user, 'Журналист'):
            person = Person.objects.get(user=request.user)
            return qs.filter(author=person)

        else:
            return qs.none()

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'author'):
            obj.author = request.user.person
        obj.save()

    # class Media:
    #     js = ('tinymce/tinymce.min.js',
    #           'tinymce/init.js', )

admin.site.register(NewsPage, NewsPageAdmin)

