from django.db import models

# Create your models here.
class Register(models.Model):
    uid = models.AutoField
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)
    lastlogin = models.DateField()

    def __str__(self):
        return self.uname