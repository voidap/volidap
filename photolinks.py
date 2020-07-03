import requests, os,random,time
token=""#токен от страницы
sl=input("Введите ссылку на альбом:\nПример скачивания альбома (album528895024_258806867)\nПример скачивания сохранёнок (album528895024_saved)\nПример скачивания фото со стены (album528895024_wall)\nПример скачивания аватарок (album528895024_profile):\n")[5:].split("_")
owner_id=sl[0]
id_album=sl[1]
a=requests.get("https://api.vk.com/method/photos.get?access_token="+token+"&v=5.92&owner_id="+owner_id+"&album_id="+id_album).json()["response"]["count"]
k=0
urls=[]
ofs=0
while k != (a//1000)+1:
    try:
        b=requests.get("https://api.vk.com/method/photos.get?access_token="+token+"&v=5.92&owner_id="+owner_id+"&album_id="+id_album+"&count=1000&offset="+str(ofs)).json()["response"]["items"]
        for x in range(1000):
            f=b[x]["id"]
            urls.append(f)
        ofs+=1000
    except:
        pass
    k+=1
print(urls)
for x in urls:
    x=str(x)
    a=open("фотки.txt","at")
    a.write("photo"+owner_id+"_"+x+"\n")
    a.close()
    print("photo"+owner_id+"_"+x)
