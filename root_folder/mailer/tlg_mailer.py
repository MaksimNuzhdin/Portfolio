import requests 
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone, tg_message):
    if TeleSettings.objects.get(pk=1):
        settings=TeleSettings.objects.get(pk=1)
        token=str(settings.tg_token)
        chatid=str(settings.tg_chat)
        text=str(settings.tg_text)
        api='https://api.telegram.org/bot'
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part1=text[0:text.find('{')]
            part2=text[text.find('}')+1:text.rfind('{')]
            part3=text[text.rfind('}')+1:text.find('(')]
            
            text_slize=part1+tg_name+part2+tg_phone+part3+tg_message
        else: text_slize=text
        # method=api+token+'/sendMessage'
        # req=requests.post(method, data={'chatid':chatid, 'text':text})
        try:
            link=f'{api}{token}/sendMessage?chat_id={chatid}&text={text_slize}'
            req=requests.post(link)
        except: pass
        finally:
            if req.status_code!=200:
                print ('Ошибка отправки')
            elif req.status_code==500:
                print ('Ошибка сервера')
            else: print ('Отправлено')
    else: pass