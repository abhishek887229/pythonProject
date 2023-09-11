from django.db import models


class Students(models.Model):
    stuid = models.IntegerField()
    stu_name = models.CharField(max_length=70)
    stu_email = models.EmailField(max_length=70)
    stu_pass = models.CharField(max_length=70)
    stu_comment = models.CharField(max_length=70)
