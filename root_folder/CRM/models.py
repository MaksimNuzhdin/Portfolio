from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name=models.CharField(max_length=200, verbose_name='Status name')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.Status_name
    class Meta:
        verbose_name='Status'
        verbose_name_plural='Statuses'
class Orders(models.Model):
    order_dt=models.DateTimeField(auto_now=True)
    order_name=models.CharField(max_length=200, verbose_name='Name')
    order_phone=models.CharField(max_length=200, verbose_name='Phone')
    order_mail=models.CharField(max_length=200, verbose_name='Mail')
    order_message=models.TextField(max_length=1000,verbose_name='message', null=True, default='New')
    status=models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')

    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.order_name
    class Meta:
        verbose_name='Order'
        verbose_name_plural='Orders'
class CommentCrm(models.Model):
    Comment_binding=models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Comment')
    Comment_text=models.TextField(verbose_name='Text comment')
    Comment_dt=models.DateTimeField(auto_now=True, verbose_name='Create date')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.Comment_text
    class Meta:
        verbose_name='Comment'
        verbose_name_plural='Commetns'