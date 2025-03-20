from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    exclude = ("img",)


class TeacherAdmin(PersonAdmin):
    pass


class MentorAdmin(PersonAdmin):
    pass


class UsefulPostAdmin(admin.ModelAdmin):
    pass


class LabAdmin(admin.ModelAdmin):
    pass


class TestAdmin(admin.ModelAdmin):
    pass


class ScheduleAdmin(admin.ModelAdmin):
    pass


class LectureAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(UsefulPost, UsefulPostAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Course, CourseAdmin)
