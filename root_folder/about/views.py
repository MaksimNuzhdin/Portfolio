from django.shortcuts import render
from .models import Discription, Networks
from education.models import Education
from projects.models import Article
from skills.models import Skills
from CRM.models import Orders
from mailer.mailer import send_mail
from mailer.tlg_mailer import sendTelegram
from resume.models import Resume
# Create your views here.
def firstpage(request):
    disc_list=Discription.objects.all()
    nw_list=Networks.objects.all()
    edu_list=Education.objects.all()
    article_list=Article.objects.order_by('-id')
    skills_list=Skills.objects.all()
    resume_list=Resume.objects.all()

    


    obj_dict={'dics_list':disc_list,'nw_list':nw_list, 'edu_list':edu_list, 
    'article_list':article_list, 'skills_list': skills_list, 'resume_list':resume_list}
    return render(request, './index.html', obj_dict)

def thanks_page(request):
    name=request.POST['name']
    phone=request.POST['phone']
    mail=request.POST['mail']
    message=request.POST['message']
    element=Orders(order_name=name, order_phone=phone, order_message=message, order_mail=mail)
    element.save()
    send_mail(receiver=mail)
    sendTelegram(tg_name=name, tg_phone=phone, tg_message=message)
    return render (request, './thanks.html', {'name': name,  'phone': phone, 'message':message, 'mail':mail})

    