from rest_framework import routers
from django.urls import path, include
from management.views import *

urls = [
    # health check
    # models handle with web View urls
    path('mangement/health/', getadminhealth),
    path('mangement/creatstudents/', creat_students),
    path('mangement/addstudents/', add_students),
    path('mangement/addsubject/', add_subject),
    path('mangement/creatsubject/', create_subject),
    path('mangement/addsubject/', add_subject),
    path('mangement/addteacher/', add_teacher),
    path('mangement/createteacher/', create_teacher),
    path('mangement/enroll/', enroll),
    path('mangement/enrollfrom/', enrollfrom),
    path('mangement/studentteacherspage/', student_teachers_page),
    path('mangement/studentteachers/', student_teachers),


    # models handle with API View urls
    path('mangement/apicreatstudents/', api_creat_students),


]