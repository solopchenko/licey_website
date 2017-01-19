from django.contrib import admin

from .models import Organisation, OrganisationBuilding, OrganisationFounder, Menu, MenuLink

# Register your models here.
class OrganisationBuildingInline(admin.StackedInline):
    model = OrganisationBuilding
    extra = 0

class OrganisationFounderInline(admin.StackedInline):
    model = OrganisationFounder
    extra = 0

class OrganisationAdmin(admin.ModelAdmin):
    inlines = (OrganisationBuildingInline, OrganisationFounderInline, )

admin.site.register(Organisation, OrganisationAdmin)

class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuLinkInline, )
    list_display = ('name', 'position', )

admin.site.register(Menu, MenuAdmin)
