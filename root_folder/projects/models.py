from django.db import models

# Create your models here.

class Article(models.Model):
    art_title=models.CharField(max_length=300, verbose_name='Title')
    sub_title=models.CharField(max_length=300,verbose_name='Sub title',default='-')
    link_to_site=models.CharField(max_length=300,verbose_name='Link to site',default='-')
    link_to_github=models.CharField(max_length=300,verbose_name='Link to github',default='-')
    art_short_disc=models.TextField(verbose_name='Short disc')
    art_image=models.ImageField(upload_to='article_img',verbose_name='Article image')

    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.art_title
    class Meta:
        verbose_name='Project'
        verbose_name_plural='Projects'
class Paragraphs(models.Model):
    par_binding=models.ForeignKey(Article,  on_delete=models.CASCADE, verbose_name='Article')
    par_text=models.TextField(verbose_name='Paragraph')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.par_text
    class Meta:
        verbose_name='Paragraph'
        verbose_name_plural='Paragraphs'
class Photo(models.Model):
    photo_binding=models.ForeignKey(Article,  on_delete=models.CASCADE, verbose_name='Article')
    photo_img=models.ImageField(upload_to='article_body_img',verbose_name='Article image')
    
    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'