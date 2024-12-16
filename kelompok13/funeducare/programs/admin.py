from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ProgramsCompetitionModel)
admin.site.register(Fee)
admin.site.register(Schedule)
admin.site.register(Teacher)
admin.site.register(Facility)
admin.site.register(Activity)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_start_date', 'program_end_date', 'description')
  
@admin.register(ParentingSeminarModel)
class ParentingSeminarAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'speaker', 'ticket_status')
    list_filter = ('ticket_status', 'date')
    search_fields = ('title', 'speaker')

@admin.register(CookingClassModel)
class CookingClassAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'instructor', 'ticket_status')
    list_filter = ('ticket_status', 'date')
    search_fields = ('title', 'instructor')

@admin.register(ChildrenExhibitionModel)
class ChildrenExhibitionAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'registration_status')
    list_filter = ('registration_status', 'date')
    search_fields = ('title', 'description')


