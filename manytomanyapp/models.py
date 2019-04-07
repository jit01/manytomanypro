from django.db import models

class student(models.Model):
    sid=models.IntegerField()
    sname = models.CharField(max_length=20)
    sloc = models.CharField(max_length=20)
    sage = models.IntegerField()
    def __str__(self):
        return self.sname

class course(models.Model):
    student = models.ManyToManyField(student)
    cname = models.CharField(max_length=20)
    fee = models.IntegerField()
    def __str__(self):
        return self.cname