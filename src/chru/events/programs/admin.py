from django.contrib import admin

from chru.events.programs.models import Program


# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }