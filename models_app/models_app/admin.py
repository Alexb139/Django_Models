from django.contrib import admin
from .models import Student, School, Department, Grade, Certificate_type
# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Certificate_type)