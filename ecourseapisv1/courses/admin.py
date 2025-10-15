from django.contrib import admin

from courses.models import Category, Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']


class Media:
    css = {
        'all': ('/static/css/style.css',)
    }

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
