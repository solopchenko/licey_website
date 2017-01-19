from django.contrib import admin

from app.utils import user_is_group_member


from .models import Person, PersonPosition, PersonTab
# Register your models here.

class PersonTabInline(admin.TabularInline):
    model = PersonTab
    extra = 0

class PersonAdmin(admin.ModelAdmin):
    fields = ('user', 'last_name', 'first_name', 'middle_name', 'office', 'positions', 'education', 'teaching_experience', 'photo', 'email', 'phone', )
    readonly_fields = ('user', 'positions', )
    inlines = (PersonTabInline, )

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        elif user_is_group_member(request.user, 'Управление сотрудниками'):
            return qs

        elif user_is_group_member(request.user, 'Сотрудник'):
            return qs.filter(user=request.user)

        else:
            return qs.filter(user=request.user)


    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.readonly_fields = tuple()

        elif user_is_group_member(request.user, 'Управление сотрудниками'):
            self.readonly_fields = tuple()

        elif user_is_group_member(request.user, 'Сотрудник'):
            self.readonly_fields = ('user', 'positions', )

        else:
            self.readonly_fields = ('user', 'positions', )

        return super(PersonAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Person, PersonAdmin)
admin.site.register(PersonPosition)
