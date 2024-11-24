from django.contrib import admin
from .models import Exam, Course, Topic, Video, List, Question, Option, Answer, Discipline, UserCourse

class CourseAdmin(admin.ModelAdmin):
  list_display = ["name", "dificulty"]

class ExamAdmin(admin.ModelAdmin):
  list_display = ["name", "year", "file"]

class TopicAdmin(admin.ModelAdmin):
  list_display = ["name", "course"]

class VideoAdmin(admin.ModelAdmin):
  list_display = ["name", "link", "description", "topic"]

class ListAdmin(admin.ModelAdmin):
  list_display = ["name"]

class QuestionAdmin(admin.ModelAdmin):
  list_display = ["task"]

class OptionAdmin(admin.ModelAdmin):
  list_display = ["text"]

class AnswerAdmin(admin.ModelAdmin):
  list_display = ["text"]

class DisciplineAdmin(admin.ModelAdmin):
  list_display = ["code", "name"]

class UserCourseAdmin(admin.ModelAdmin):
  list_display = ["user", "course", "status"]

admin.site.register(Course, CourseAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(List,ListAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(UserCourse, UserCourseAdmin)