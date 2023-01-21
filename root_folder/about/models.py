from django.db import models

# Create your models here.
class Discription(models.Model):
    disc=models.TextField(verbose_name='text')
    dics_image=models.ImageField(upload_to='about_img', null=True)
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.disc
    class Meta:
        verbose_name='Discription'
        verbose_name_plural='Discription'
class Networks(models.Model):
    nw_name=models.CharField(max_length=100, verbose_name='Network')
    nw_link=models.CharField(max_length=200, verbose_name='link')
    nw_image=models.ImageField(upload_to='Networks_img')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.nw_name
    class Meta:
        verbose_name='Network'
        verbose_name_plural='Networks'