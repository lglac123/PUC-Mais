from django.contrib import admin
from .models import Exam, Course, Topic, Video, List, Question, Option, Answer

class CourseAdmin(admin.ModelAdmin):
  list_display = ["name", "dificulty"]

class ExamAdmin(admin.ModelAdmin):
  list_display = ["name", "year", "file"]

class TopicAdmin(admin.ModelAdmin):
  list_display = ["name", "course"]

class VideoAdmin(admin.ModelAdmin):
  list_display = ["name", "link", "description", "topic"]

class ListAdmin(admin.ModelAdmin):
  list_display = ["name", "topic"]

class QuestionAdmin(admin.ModelAdmin):
  list_display = ["task"]

class OptionAdmin(admin.ModelAdmin):
  list_display = ["text"]

class AnswerAdmin(admin.ModelAdmin):
  list_display = ["text"]

admin.site.register(Course, CourseAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(List,ListAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Answer, AnswerAdmin)