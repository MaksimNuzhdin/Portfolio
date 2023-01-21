from django.db import models

# Create your models here.
class Skills(models.Model):
    skill_name=models.CharField(max_length=200, verbose_name='Name')
    skill_photo=models.ImageField(upload_to='skills_img')
    skill_disc=models.TextField(verbose_name='Discription')
    skill_comp=models.TextField(verbose_name='Competencies', null=True)
    
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.skill_name
    class Meta:
        verbose_name='Skill'
        verbose_name_plural='Skills'
