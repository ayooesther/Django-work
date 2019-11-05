from django.contrib import admin

from.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
        list_display =("first_name","last_name","gender","email","phone_number")
        search_fields =("first_name","last_name","gender","email","phone_number")


admin.site.register(Teacher,TeacherAdmin)    
