from django.db import models

# Create your models here.
class Education(models.Model):
    edu_name=models.CharField(max_length=200, verbose_name='Name')
    edu_image=models.ImageField(upload_to='edu_image',verbose_name='Image')
    edu_disc=models.TextField(verbose_name='Discription')
    edu_start=models.CharField(max_length=200, verbose_name='Start date')
    edu_end=models.CharField(max_length=200, verbose_name='End date')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.edu_name
    class Meta:
        verbose_name='Education'
        verbose_name_plural='Education'