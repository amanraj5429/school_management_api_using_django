from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    admission_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15,null=False, blank=False, default='TBU')
    emergency_contact = models.CharField(max_length=15,null=False, blank=False, default='TBU')
    parent_guardian = models.CharField(max_length=10,null=False, blank=False, default='TBU')
    # Add other fields like contact information, emergency contacts, and parent/guardian information as needed

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade_value = models.CharField(max_length=2)
    # Add other fields like comments, date recorded, etc.

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])
    # Add other fields like subject-specific attendance



class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # You should hash and salt the passwords.
    role = models.CharField(max_length=20, choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Administrator')])
    # Add other user-related fields

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Subject = models.CharField(max_length=10, default='TBU')
    # Add teacher-related fields
