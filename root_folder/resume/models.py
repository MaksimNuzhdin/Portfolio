from django.db import models

# Create your models here.
class Resume(models.Model):
    resume_name=models.CharField(max_length=100, verbose_name='Name of resume')
    resume_language=models.CharField(max_length=100, verbose_name=' Language of resume')
    resume_file=models.FileField(verbose_name='File', upload_to='resume_files')
    resume_img=models.ImageField(verbose_name='Image', upload_to='resume_images', null=True)
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.resume_name
    class Meta:
        verbose_name='Resume'
        verbose_name_plural='Resume'