# -*- coding: utf-8 -*-
import vk_api,random,requests,glob,time,json
from vk_api.longpoll import VkLongPoll, VkEventType, VkChatEventType
from threading import Thread
from vk_api.longpoll import VkLongPoll, VkEventType, VkChatEventType
tkn = "fe58536077d31aea58ce32023fe4788de2bd1ae00cb4870177b026abd9059574cc1fc8aad667002c255b2"#токен бота
idvk = 400945113#айди бота
ignorelist = []#игнор пользователей
conf = [599246827]#игнор бесед
invusers=[434762691,281103195]#пользователи, которых нужно приглашать
title1=["Пизди хахлов"]#Названия кф
photo = "photo.jpg"
vk_session = vk_api.VkApi(token=tkn)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def friends():
    while True:
        try:
            zayavki=vk.friends.getRequests(v=5.92)['items']
            for u in zayavki:
                vk.friends.add(user_id=u)
        except:
            pass
        try:
            zayavki1=vk.friends.getRequests(out="true")['items']
            for u in zayavki1:
                vk.friends.delete(user_id=u)
        except:
            pass
        time.sleep(10)
class m(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        self.a = a
    def run(self):
        print(self.a)
        while True:
            try:
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.user_id != idvk:
                        peer_id = event.peer_id
                        user_id = event.user_id
                        b=event.text
                        c=random.choice([1,2])
                        if c == 1 and event.user_id > 0 and event.user_id != idvk:
                            if peer_id > 2000000000 and not event.chat_id in conf and not event.user_id in ignorelist:
                                f = open('фразы.txt',encoding='utf-8', errors='ignore')
                                data1 = f.read()
                                msg = random.choice(data1.split('\n'))
                                g = open('фотки.txt',encoding='utf-8', errors='ignore')
                                data2 = g.read()
                                photo = random.choice(data2.split('\n'))
                                vk.messages.setActivity(peer_id=peer_id,type='typing')
                                time.sleep(random.randint(1,3))
                                vk.messages.send(peer_id=peer_id,random_id=random.randint(100000,999999),message=msg,attachment=random.choice([str(photo),'','','','']))
                            elif peer_id < 2000000000 and user_id > 0:
                                if b[0:8] == "https://":
                                    print(vk.messages.joinChatByInviteLink(link=b))
                                else:
                                    if not event.user_id in ignorelist:
                                        f = open('фразы.txt',encoding='utf-8', errors='ignore')
                                        data = f.read()
                                        msg = random.choice(data.split('\n'))
                                        g = open('фотки.txt',encoding='utf-8', errors='ignore')
                                        data2 = g.read()
                                        photo = random.choice(data2.split('\n'))
                                        vk.messages.setActivity(peer_id=peer_id,type='typing')
                                        time.sleep(random.randint(1,3))
                                        vk.messages.send(peer_id=peer_id,random_id=random.randint(100000,999999),message=msg,attachment=random.choice([str(photo),'','','','']))
                        if c == 2 and event.user_id > 0 and event.user_id != idvk:
                            if peer_id > 2000000000 and not event.chat_id in conf and not event.user_id in ignorelist:
                                a=vk.docs.getMessagesUploadServer(type='audio_message',peer_id=user_id)['upload_url']
                                try:
                                    say=random.choice(glob.glob("voice/*.ogg"))
                                except:
                                    say=random.choice(glob.glob("voice/*.mp3"))
                                img = {'file': ('a.mp3', open(say, 'rb'))}
                                response = requests.post(a, files=img)
                                result = json.loads(response.text)['file']
                                owner=vk.docs.save(file=result)['audio_message']['owner_id']
                                document=vk.docs.save(file=result)['audio_message']['id']
                                send = 'doc'+str(owner)+'_'+str(document)
                                vk.messages.setActivity(peer_id=peer_id,type="audiomessage")
                                time.sleep(random.randint(1,3))
                                vk.messages.send(random_id=random.randint(100000,999999),attachment=send,peer_id=peer_id)
                            elif peer_id < 2000000000:
                                if b[0:8] == "https://":
                                    print(vk.messages.joinChatByInviteLink(link=b))
                                else:
                                    if not event.user_id in ignorelist:
                                        a=vk.docs.getMessagesUploadServer(type='audio_message',peer_id=user_id)['upload_url']
                                        try:
                                            say=random.choice(glob.glob("voice/*.ogg"))
                                        except:
                                            say=random.choice(glob.glob("voice/*.mp3"))
                                        img = {'file': ('a.mp3', open(say, 'rb'))}
                                        response = requests.post(a, files=img)
                                        result = json.loads(response.text)['file']
                                        owner=vk.docs.save(file=result)['audio_message']['owner_id']
                                        document=vk.docs.save(file=result)['audio_message']['id']
                                        send = 'doc'+str(owner)+'_'+str(document)
                                        vk.messages.setActivity(peer_id=peer_id,type="audiomessage")
                                        time.sleep(random.randint(1,3))
                                        vk.messages.send(random_id=random.randint(100000,999999),attachment=send,peer_id=peer_id)
                    namekf=vk.messages.getChat(chat_id=int(event.peer_id)-2000000000)["title"]
                    if not namekf in title1 and not int(event.peer_id)-2000000000 in conf:
                        vk.messages.editChat(chat_id=event.chat_id,title=random.choice(title1))
                        j=vk.photos.getChatUploadServer(chat_id=int(event.peer_id)-2000000000,crop_x=10,crop_y=25)['upload_url']
                        img = {'photo': ("photo.jpg", open("photo.jpg", 'rb'))}
                        response = requests.post(j, files=img)
                        result = json.loads(response.text)['response']
                        vk.messages.setChatPhoto(file=result)
                    break
            except Exception as e:
                if str(e) == "Captcha needed":
                    sec_sleep=random.randint(15,40)
                    print("Бот словил каптчу. Сон на",sec_sleep,"секунд!")
                    time.sleep(sec_sleep)
                    print("Бот снова работает!")
class m1(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        self.a = a
    def run(self):
        print(self.a)
        while True:
            try:
                for event in longpoll.listen():
                    f=vk.messages.getById(message_ids=event.message_id)["items"][0]["action"]["type"]
                    if str(f) == 'chat_kick_user':                      
                        vk.messages.addChatUser(chat_id=event.chat_id,user_id=event.user_id)
            except:
                pass
class m2(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        self.a = a
    def run(self):
        print(self.a)
        while True:
            try:
                for event in longpoll.listen():
                    if event.type_id == VkChatEventType.USER_JOINED and event.info['user_id'] == idvk:
                        f = open('фразы.txt',encoding='utf-8', errors='ignore')
                        data1 = f.read()
                        msg = random.choice(data1.split('\n'))
                        idmsg=vk.messages.send(peer_id=event.peer_id,random_id=random.randint(100000,999999),message=msg)
                        vk.messages.pin(peer_id=event.peer_id,message_id=idmsg)
                        for x in invusers:
                            vk.messages.addChatUser(chat_id=event.chat_id,user_id=x)
            except:
                pass
class f(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        self.a = a
    def run(self):
        print(self.a)
        friends()

f("Проверка друзей запущена!").start()
m("Отправка сообщений запущена!").start()
m1("Инвайт друзей, если их кикают или если они ливают, включен!").start()
m2("Действия по приглосу в конфу запущены!").start()
