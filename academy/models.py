from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    duration = models.IntegerField(help_text="duration in hourse")
    course_image = models.ImageField(upload_to="courses/" ,blank= True, null=True)
    
    def __str__(self):
        return self.course_name
    
class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    expersite = models.CharField(max_length=50)
    Trainer_photo = models.ImageField(upload_to="Trainers/", blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
   
    enrolled_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        