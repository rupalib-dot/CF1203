from django.contrib import admin
from course_management.models import Course,Category,Chapter,CourseAlloted

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(CourseAlloted)