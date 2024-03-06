from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    up_dated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
