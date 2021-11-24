from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=255)
    eemail = models.CharField(max_length=255)
    econtact = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"

class User(models.Model):
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=255)
    uemail = models.CharField(max_length=255, default='SOME STRING')
    password = models.CharField(max_length=30, default='SOME INT')
    repassword = models.CharField(max_length=30, default='SOME INT')
    class Meta:
        db_table = "user"