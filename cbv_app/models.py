from django.db import models

class School(models.Model):
    name        = models.CharField(max_length=256)
    principal   = models.CharField(max_length=256)
    location    = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    name    = models.CharField(max_length=256)
    age     = models.PositiveIntegerField()
    school  = models.ForeignKey(School,related_name='students_item', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# Create your models here.
