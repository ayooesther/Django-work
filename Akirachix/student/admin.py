from django.contrib import admin

from.models import Student



class StudentAdmin(admin.ModelAdmin):
        list_display =("registration","first_name","last_name","date_of_birth","email")
        search_fields =("registration","first_name","last_name","date_of_birth","email")


admin.site.register(Student,StudentAdmin)    