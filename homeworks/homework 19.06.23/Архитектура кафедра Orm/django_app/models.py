from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    image = models.ImageField("Изображение", upload_to="images/posts")

    def __str__(self):
        return f"{self.name} {self.surname}"




class Professor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10)
    profession = models.CharField(max_length=100)  # Кафедра
    number = models.CharField(max_length=100)
    nationality = models.TextField()
    image = models.ImageField("Изображение", upload_to="images/posts")

    def __str__(self):
        return f"{self.name} {self.surname}"


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teachers = models.CharField(max_length=255)


    def __str__(self):
        return self.title
