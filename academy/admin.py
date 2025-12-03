from django.contrib import admin
from .models import Course, Trainer, Student


class CourseAdnmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration')
    
class TrainearAdimn(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','expersite', 'email')   

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email', 'is_active', 'enrolled_course', 'trainer')
    
admin.site.register(Course, CourseAdnmin)
admin.site.register(Trainer, TrainearAdimn)
admin.site.register(Student, StudentAdmin)