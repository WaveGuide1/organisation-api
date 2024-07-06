from django.contrib import admin
from .models import Organisation


# Register your models here.

class OrganisationAdmin(admin.ModelAdmin):
    readonly_fields = ('orgId',)


admin.site.register(Organisation, OrganisationAdmin, )

