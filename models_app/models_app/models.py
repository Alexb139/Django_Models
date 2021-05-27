from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here


        #ForeignKey (Faculty)
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=40)


    def __str__(self):
        return self.faculty_name



        #ForeignKey (Department)
class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=400)
    


    def __str__(self):
        return self.department_name



        #ForeingKey (School)
class School(models.Model):
    school_name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    postal_code = models.IntegerField()


    def __str__(self):
        return self.school_name



        #ForeignKey (Grade)
class Grade(models.Model):
    grade_type = models.CharField(max_length=40)


    def __str__(self):
        return self.grade_type



        #ForeignKey (Certificate Type)
class Certificate_type(models.Model):
    certificate_type_name = models.CharField(max_length=200)


    def __str__(self):
        return self.certificate_type_name




class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    year_of_graduation = models.IntegerField()
    
    

    def __str__(self):
        return self.full_name
        
