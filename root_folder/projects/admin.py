from django.contrib import admin
from .models import Article, Paragraphs,Photo
# Register your models here.
class AdmParagraphs(admin.StackedInline):
    model= Paragraphs
    fields=('par_text',)
    extra=1
class AdmPhoto(admin.StackedInline):
    model=Photo
    extra=1    
    
class AdmArticle(admin.ModelAdmin):
    inlines=[AdmParagraphs,AdmPhoto]
admin.site.register(Article,AdmArticle)# регистритруем приложение на сайт
admin.site.register(Paragraphs,)
admin.site.register(Photo, )
