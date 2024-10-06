from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'link_to_video', 'course')
    list_filter = ('name', 'course',)
    search_fields = ('name', 'course',)
