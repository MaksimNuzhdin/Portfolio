from django.contrib import admin
from .models import CommentCrm, Orders,StatusCrm
# Register your models here.
class Comment(admin.StackedInline):
    model= CommentCrm
    fields=('Comment_dt','Comment_text')
    readonly_fields=('Comment_dt',)
    extra=1
class OrderAdm(admin.ModelAdmin):
    list_display=('id','status', 'order_name','order_phone','order_mail','order_dt')
    list_display_links=('id','order_name')
    search_fields=('id', 'order_name','order_phone','order_dt')
    list_filter=('status',)
    list_editable=('status',)
    list_per_page=10
    list_max_show_all=100
    list_per_page=10
    list_max_show_all=100
    fields= ('id','status', 'order_name','order_phone','order_mail','order_dt','order_message')
    readonly_fields=('id','order_dt')
    inlines=[Comment,]

admin.site.register(Orders,OrderAdm)# регистритруем приложение на сайт
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)