from django.db import models
from datetime import datetime
first_name = models.CharField(max_length=30)
last_name = models.CharField(max_length=30)

# Create your models here

class School(models.Model):
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    postal_code = models.IntegerField()


    def __str__(self):
        return self.name

class Student(models.Model):
    School = models.ForeignKey(School, on_delete=models.Cascade)
    first_name +last_name = models.CharField(max_length=60)
    Grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    year_of_graduation = models.IntegerField()
    date_of_resumption = models.DateField(default=datetime.today)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_type, on_delete=models.Cascade)



    def __str__(self):
        return self.first_name+last_name


class Grade(models.Model):
    grade_type = models.IntegerField()


    def __str__(self):
        return self.grade_type



class Department(models.Model):
    department_name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name