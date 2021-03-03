import urllib.request
import json
import os
import banner
os.system("clear")
print()
print(banner.banner)
print()
print("   ")
print("АВТОР: t.me/VedmakRussia228")
print("узнайте информацию об айпи адресе!")
getIP = input("{•_•} Введите айпи > ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen( url )

except:
    print( "  " )
    print( "\n                     НЕВЕРНЫЙ АЙПИ! \n" )
    print( " " )
    print( " " )
    os.system("python ip-info.py")

infoList = json.load(getInfo)

def whoisIPinfo(ip):

    try:

        myComand = "whois " + getIP
        whoisInfo = os.popen( myComand ).read()
        return whoisInfo

    except:

        return "\n [×_ ×] — Ошибка — [× _×] \n"

     
print( "-" * 60 )
try:
	print( "Айпи: ", infoList["ip"] )
	print( "Город: ", infoList["city"] )
	print( "Регион: ", infoList["region"] )
	print( "Страна: ", infoList["country"] )
	print( "ИмяХоста: ", infoList["hostname"] )
	print( "-" * 60 )
	print( "-" * 60)
	print( whoisIPinfo ( getIP ) )
	print( "ДЛЯ ПОВТОРНОГО ПОИСКА ПЕРЕЗАПУСТИТЕ УТИЛИТУ [°∆°]")
except:
	print( " кое что не удалось найти... " )
	print( " [^¢^] перезапустите утилиту если желаете пробить еще один айпи адресс " )