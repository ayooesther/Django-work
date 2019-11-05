from django.contrib import admin

from.models import Course


class CourseAdmin(admin.ModelAdmin):
        list_display =("duration_months","start_date","end_date","description","teacher")
        search_fields =("duration_months","start_date","end_date","description","teacher__first_name")


admin.site.register(Course,CourseAdmin)    