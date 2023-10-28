# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('students/', views.student_list, name='student-list'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('courses/', views.course_list, name='course-list'),
    path('courses/<int:pk>/', views.course_detail, name='course-detail'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='course-detail'),
    path('teachers/', views.teacher_list, name='teacher-list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher-detail'),
    path('grades/', views.grade_list, name='grade-list'),
    path('grades/<int:pk>/', views.grade_detail, name='grade-detail'),
    path('attendence/',views.attendence_list, name='attendence-list'),
    path('attendence/<int:pk>/', views.attendence_detail, name='attendence-detail'),
]