from django.contrib import admin
from management.models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(SubjectStudentMap)
admin.site.register(Subject)