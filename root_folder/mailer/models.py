from django.db import models
# Create your models here.
class MSettings(models.Model):
    mail_title=models.CharField(max_length=300, verbose_name= 'Title')
    mail_h1=models.CharField(max_length=300, verbose_name='h1 title')
    mail_text=models.TextField(verbose_name='Text')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.mail_title
    class Meta:
        verbose_name='Mail'
        verbose_name_plural='Mail'
class TeleSettings(models.Model):
    tg_token=models.CharField(max_length=200, verbose_name='Token')
    tg_chat=models.CharField(max_length=200, verbose_name='Chat')
    tg_text=models.TextField(verbose_name='Text')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.tg_chat
    class Meta:
        verbose_name='Telegram'
        verbose_name_plural='Telegram'