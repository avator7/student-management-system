from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, request
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.utils import json
from django.http import HttpResponse, HttpRequest
from .models import *
from django.contrib import messages

# Create your views here.
@api_view(['GET'])
def getadminhealth(requests):
    return Response("ok")



def add_students(requests):
    return render(requests, 'student.html')


@api_view(['POST'])
def api_creat_students(requests):
    data = requests.data
    fname=str(data['fname'])
    lname=str(data['lname'])
    dob=str(data['dob'])
    number=str(data['number'])
    address=str(data['address'])

    students = Student(first_name=fname, last_name=lname, dob=dob, address=address, phone=number)
    students.save()
    return Response('student created successfully', status=200)



@api_view(['POST'])
def creat_students(requests):
    if requests.method=='POST':
        fname=requests.POST['fname']
        lname=requests.POST['lname']
        dob=requests.POST['dob']
        number=requests.POST['number']
        address=requests.POST['address']
    students = Student(first_name=fname, last_name=lname, dob=dob, address=address, phone=number)
    students.save()
    messages.success(requests, "Your Student has been created successfully")
    return render(requests, 'student.html')



def add_subject(requests):
    return render(requests, 'subject.html')

# def api_creat_subject(requests):
#     data = requests.data
#     name = str(data['name'])
#     textbook = str(data['textbook'])
#     subject = Subject(name=name, textbook=textbook)
#     subject.save()
#     return Response('subject created successfully', status=200)


@api_view(['POST'])
def create_subject(requests):
   
    if requests.method=='POST':
        name=requests.POST['name']
        textbook=requests.POST['textbook']
    subject = Subject(name=name, textbook=textbook)
    subject.save()
    messages.success(requests, "Your Subject has been created successfully")
    # return render(requests, 'subject.html')
    return Response('subject created successfully', status=200)


def add_teacher(requests):
    subjects = Subject.objects.all()
    return render(requests, 'teacher.html',{'subjects':subjects})


@api_view(['POST'])
def create_teacher(requests):
    if requests.method=='POST':
        name=requests.POST['name']
        subject=requests.POST['subject']
    sub = Subject.objects.filter(name=subject).first()
    teacher = Teacher(name=name,subject=sub )
    teacher.save()
    messages.success(requests, "Your Teacher has been created successfully")
    return Response('teacher created successfully', status=200)


@api_view(['POST'])
def enroll(requests):
    if requests.method=='POST':
        student = requests.POST['student']
        subject = requests.POST['subject']
    student_name= student.split(' ')
    sub = Subject.objects.filter(name=subject).first()
    students = Student.objects.filter(first_name__contains=student_name[0], last_name__contains=student_name[1]).first()
    chossed_subject = SubjectStudentMap(student=students, subject=sub)
    chossed_subject.save()
    return Response("Student enrolled ", status=200)

def enrollfrom(requests):
    student =  Student.objects.all()
    subject = Subject.objects.all()
    return render(requests, 'enroll.html',{'student': student,'subject': subject})



def student_teachers_page(requests):
    student =  Student.objects.all()
    return render(requests, 'studentteachers.html',{'student': student})


@api_view(['GET','POST'])
def student_teachers(requests):
    if requests.method=='POST':
        student = requests.POST['student']
    student_name= student.split(' ')
    students = Student.objects.filter(first_name__contains=student_name[0], last_name__contains=student_name[1]).first()
    subjects = SubjectStudentMap.objects.filter(student_id=students.pk).values_list('subject_id', flat=True)
    teachers = Teacher.objects.filter(subject__in=subjects)
    print(students.pk,subjects,teachers)
    return render(requests, 'studentteachers.html',{'teachers': teachers})
    # return Response('ok', status=200)
    