from django.contrib import admin
from .models import Exam, Course

class CourseAdmin(admin.ModelAdmin):
  list_display = ["name", "dificulty"]

class ExamAdmin(admin.ModelAdmin):
  list_display = ["name", "year", "file"]

admin.site.register(Course, CourseAdmin)
admin.site.register(Exam, ExamAdmin)