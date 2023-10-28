from django.contrib import admin
from .models import Student, Course, Grade, Attendance, Teacher, User
# Register your models here.


admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Attendance)
admin.site.register(Teacher)
admin.site.register(User)