from django.db import models


class TeacherInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    age  = models.IntegerField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name