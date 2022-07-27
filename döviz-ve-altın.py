#Hürriyet'ten döviz ve altın verilerini çekmek için yapılmış bir script
#Belki çok verimli değildir kod,ama küçük bir iş için abartmaya gerek yok
#Çok eski bir kod olduğu için optimize edilecek bir şey görürseniz PR yapmaktan çekinmeyin

yenileme=60#Kaç saniyede bir yenilemesini söyler
tekrar=10#Kaç saniyede bir tekrar denemesini söyler

from requests import get
from bs4 import BeautifulSoup
from time import sleep
from numpy import empty,append




dolar=[]
euro=[]
sterlin=[]
gr=[]
çey=[]
ons=[]
while True:
    d=False
    d2=False
    try:
        site=get("https://bigpara.hurriyet.com.tr/doviz/")
        d=True
    except:
        try:
            site = get("https://bigpara.hurriyet.com.tr/doviz/")
            d = True
        except:
            print("Siteye ulaşılamadı,lüften internet bağlantınızdan emin olun (Döviz)")
            sleep(tekrar)
            continue
    if d:
        içerik=BeautifulSoup(site.content,"html.parser")
        liste0 = içerik.find_all("span", {"class": "value"})
        dalış=float(liste0[1].text.replace(",", "."))
        dsatış = float(liste0[2].text.replace(",", "."))
        ealış = float(liste0[4].text.replace(",", "."))
        esatış = float(liste0[5].text.replace(",", "."))
        salış = float(liste0[7].text.replace(",", "."))
        ssatış = float(liste0[8].text.replace(",", "."))
        dolar.append(dalış)
        euro.append(ealış)
        sterlin.append(salış)
    try:
        site3=get("https://bigpara.hurriyet.com.tr/altin/")
        d2=True
    except:
        try:
            site3 = get("https://bigpara.hurriyet.com.tr/altin/")
            d2 = True
        except:
            print("Siteye ulaşılamadı,lüften internet bağlantınızdan emin olun (Altın)")
            sleep(tekrar)
            continue

    if d2:
        içerik2 = BeautifulSoup(site3.content, "html.parser")
        liste = içerik2.find_all("span", {"class": "value"})
        gralış=float(liste[1].text.replace(",", "."))
        grsatış = float(liste[2].text.replace(",", "."))
        çalış=float(liste[4].text.replace(".", "").replace(",", "."))
        çsatış=float(liste[5].text.replace(".", "").replace(",", "."))
        talış=float(liste[7].text.replace(".", "").replace(",", "."))
        tsatış=float(liste[8].text.replace(".", "").replace(",", "."))
        gr.append(gralış)
        çey.append(çalış)
        ons.append(talış)
        uzak=len(dolar)

        

        print("Dolar: Alış:{} Satış:{}".format(dalış, dsatış))
        print("Euro: Alış:{} Satış:{}".format(ealış, esatış))
        print("Sterlin: Alış:{} Satış:{}".format(salış, ssatış))
        print("Gram Altın: Alış:{} Satış:{}".format(gralış, grsatış))
        print("Çeyrek Altın: Alış:{} Satış:{}".format(çalış, çsatış))
        print("ONS Altın: Alış:{} Satış:{}".format(talış, tsatış))
        print("                                                     ")
        sleep(yenileme)
    try:
        pass

    except:
        print("Sıkıntı çıktı.")
        sleep(tekrar)
    

