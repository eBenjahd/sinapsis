from django.db import models

class Teacher(models.Model):

    name = models.CharField(max_length=100, verbose_name='teacher')
    email = models.EmailField(unique=True)
    specialty = models.CharField(max_length=100, verbose_name='specialty')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Teacher {self.name}'