__author__ = 'Ammar Ahmed ALYASRY'
# !/usr/bin/env python
# -*- coding: cp1254 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import json
import time, locale
from PyQt4 import QtCore, QtGui
yerler={"A1":"free","A2":"free","A3":"free","A4":"free","A5":"free","A6:":"free","A7":"free","A8":"free","A9":"free","A10":"free","B1":"free","B2":"free","B3":"free","B4":"free",              "B5":"free","B6":"free","B7":"free","B8":"free","B9":"free","B10":"free","C1":"free","C2":"free","C3":"free","C4":"free","C5":"free","C6":"free","C7":"free","C8":"free",                 "C9":"free","C10":"free","D1":"free","D2":"free","D3":"free","D4":"free","D5":"free","D6":"free","D7":"free","D8":"free","D9":"free","D10":"free","E1":"free","E2":"free",              "E3":"free","E4":"free","E5":"free", "E6":"free","E7":"free","E8":"free","E9":"free","E10":"free"}
#yukarda bir dictionary olarak yaptim her yer bostur : bunun mantigini Savastan baktim : Ugur hoca da yardim etti
dosya = open('arabalar.json','a') #arabalar isimli bir json dosya actim

listofyerler=["A1","A2","A3","A4","A5","A6:","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1",                          "C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8",                                                  "D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10"] #bu listede yukarda yaptigim dictionary degerleri cektim

# ---------- Bu alanda değişiklik yapmayınız --------
class Otopark_Otomasyonu(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Otopark_Otomasyonu, self).__init__(parent) #burada birkac degisiklik yaparak acilan pencerenin buyutulmasini sagladim

# --------  istenen değerleri burada tanımlanıyor ----------
        self.plaka = QLabel('Plaka')
        self.plaka.setStyleSheet("background-color: rgb(200, 30, 200);")#bu saatir renk veriyor

        self.TL = QLabel('TL')
        self.cm=QLabel('m')

        self.yukseklik = QLabel('Yükseklikk')
        self.yukseklik.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.yer = QLabel('Yer')
        self.yer.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.gSaat = QLabel('Giriş Saati')
        self.gSaat.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.fiyat=QLabel('fiyat TL')
        self.fiyat.setStyleSheet("background-color: rgb(200, 30, 200);")

        self.cikisSaat=QLabel('cikis saat')
        self.cikisSaat.setStyleSheet("background-color: rgb(200, 30, 200);")
#????? ??????



# -------- Formun istenen değerleri tanımlama buraya kadar ---------
# 1) .......

# ------- Formda kullanıcıdan alınan değerler ---------
        self.plakasi = QLineEdit()
        self.plakasi.setMinimumSize(QtCore.QSize(270, 30)) #burada textbox daha genis haline getirir
        self.plakasi.setMaximumSize(QtCore.QSize(270, 30))



        self.yuksekligi = QLineEdit()
        self.yuksekligi.setInputMask('0.9')     # nokta koymak icin koydum
        self.yuksekligi.setMinimumSize(QtCore.QSize(30, 30))
        self.yuksekligi.setMaximumSize(QtCore.QSize(30, 30))


        self.yeri = QLineEdit()
        self.yeri.setReadOnly(True) #burada onemli bir yer cunki texbox durumu sadece okumak icin olsun yani orada degisiklik yaplamaz
        self.yeri.setStyleSheet("background-color: rgb(4, 200, 186);")
        self.yeri.setMinimumSize(QtCore.QSize(270, 30))
        self.yeri.setMaximumSize(QtCore.QSize(270, 30))

        self.gSaati = QLineEdit()
        self.gSaati.setReadOnly(True)
        self.gSaati.setStyleSheet("background-color: rgb(4, 200, 186);")


        self.fiyati=QLineEdit()
        self.fiyati.setReadOnly(True)
        self.fiyati.setStyleSheet("background-color: rgb(4, 200, 186);")
        self.fiyati.setAlignment(QtCore.Qt.AlignCenter)
        self.fiyati.setMaximumSize(QtCore.QSize(30, 30))
        self.fiyati.setMinimumSize(QtCore.QSize(30, 30))


        #self.fiyati.setMinimumSize(QtCore.QSize(30, 30))
        #self.fiyati.setMaximumSize(QtCore.QSize(30, 30))
        self.cikisSaati=QLineEdit()
        self.cikisSaati.setReadOnly(True)
        self.cikisSaati.setStyleSheet("background-color: rgb(4, 200, 186);")

        self.kaydet = QPushButton('Giris')
        #self.kaydet.setStyleSheet("background-color: rgb(200,10,100 );")

        self.cikis= QPushButton('Cikis')

        #self.connect(self.cikis, SIGNAL('pressed()'), self.topla)
        self.connect(self.cikis, SIGNAL('pressed()'), self.zaman2)
        self.connect(self.kaydet, SIGNAL('pressed()'), self.zaman)    # Kaydet butonuna tıklandığu anda ekle isimli bir fonksiyon çağrılır.
        #self.connect(self.cikis, SIGNAL('pressed()'), self.ekle)
        #self.connect(self.cikis, SIGNAL('pressed()'), self.ucret)


# ---------- Yukarıdaki kodu değiştirmeyiniz. Ancak ekleme yapabilirsiniz. --------
        izgara = QGridLayout()
        izgara.addWidget(self.plaka, 0, 0,)
        izgara.addWidget(self.yukseklik, 1, 0,)
        izgara.addWidget(self.yer, 2, 0,)
        izgara.addWidget(self.gSaat, 3, 0,)
        izgara.addWidget(self.fiyat, 4, 0,)
        izgara.addWidget(self.cikisSaat,5,0,)


        izgara.addWidget(self.plakasi, 0, 1,)
        izgara.addWidget(self.yuksekligi, 1, 1,)
        izgara.addWidget(self.yeri, 2, 1,)
        izgara.addWidget(self.gSaati, 3, 1,)
        izgara.addWidget(self.fiyati,4,1,)

        izgara.addWidget(self.TL,4,2)
        izgara.addWidget(self.cm,1,2)


        izgara.addWidget(self.cikisSaati,5,1,)

        izgara.addWidget(self.kaydet, 6, 0,)
        izgara.addWidget(self.cikis, 6, 1,)

        self.setLayout(izgara)
        self.setWindowTitle('Otopark Otomasyonu, Araç Formu')



    def topla(self):            #burasi deneme yapmak icin yaptim
       a=self.plakasi.text()
       b=self.fiyati.text()
       c=int(a)+int(b)
       self.yeri.setText(str(c))





    def zaman(self):            #burasi giris fonksiyonun basladigi yer

        dosya3=open('arabalar.json')# yukarda olusturmus oldugum dosyayi okuyor



        if self.plakasi.text()!="" and self.yuksekligi.text()!="." : #burada kullanici plaka ve yukseklik bos brakmasin diy
            buyukise=float(self.yuksekligi.text())
            if (buyukise<2.4): #burda zaten belli
                self.gSaati.setText(time.strftime("%H:%M:%S")) #giris zamani yaziyor

                for i in listofyerler:
                    infilevarmi=0  #bu islem ise kaldigimiz yerden devam  etmek icin : Adil hocanin yardimiyla
                    dosya3.seek(0,0) #dosyanin basina getirmek icin yaptim
                    for m in dosya3:
                        veri=json.loads(m)


                        if veri['citys']['yeri']==i:
                            infilevarmi=1
                            break
                    if infilevarmi==1:
                        yerler[i]="full"       #burada bir islem yapildiginda free olan yeri bos kalsin
                        continue
                    elif infilevarmi==0 and yerler[i]=="free":
                         yerler[i]="full"
                         print(yerler)
                         self.yeri.setText(i)
                         dosya.write('{"citys":'+ '{'+'"yeri"'+':'+'"'+i+'"' +',' +'"numarasi"'+':'+ '"'+ self.plakasi.text()+'"' + ',' + '"zaman"'+':'+'"'+ time.strftime("%H:%M:%S") + '"'+','+'"yukseklikleri"'+':'+ self.yuksekligi.text() +'0'+'}}'+ '\n')
                         #yukardaki iki satirda girilen verileri json dosyasina actirdim
                         self.plakasi.setText("")
                         self.gSaati.setText("")    #islem bittikten sonra texboxlar bosalsin
                         self.yuksekligi.setText("")

                         break
            else:
                self.plakasi.setStyleSheet("background-color: rgb(250, 10, 25);")
                self.plakasi.setText('Yukseklugi 2.4ten buyuk bir araba girdiniz!!!. girilmez ')    #yuksekligi 2.4den buyuk ise texboxu kirmizi yapip bir uyari versin
                #time.sleep(3)  #burda 3 saniye uyuyup kapansin istedim ama olmadi
                #exit()


        else:
            self.plakasi.setStyleSheet("background-color: rgb(250, 10, 25);")   #bu da texboxlari bos oldugunda oyle bir uyari versin
            self.plakasi.setText('Plakasi ve yksekligi giriniz !!!!')
            #time.sleep(3)
            #exit()

        dosya3.close()








    def zaman2(self):               #burasi cikis fonksiyonudur

        self.cikisSaati.setText(time.strftime("%H:%M:%S"))  #cikis saati yaziyor


        import json
        acmak=open("arabalar.json") #olusturdugum dosyayi tekrer aciyor ve satirlari okuyor
        for doc in acmak:
            veriler = json.loads(doc)

            if (veriler['citys']['numarasi']==self.plakasi.text()): #burada zaten belli
                self.cikisSaati.setText(time.strftime("%H:%M:%S"))
                self.gSaati.setText(veriler['citys']['zaman'])  #buralarda bilgileri yaziyor
                self.yeri.setText(veriler['citys']['yeri'])


                girisZamani=veriler['citys']['zaman']

                a=girisZamani[0]
                b=girisZamani[1]
                c=a+b
                c=int(c)

                f=girisZamani[3]
                t=girisZamani[4]
                d=f+t
                d=int(d)

                cikisZamani=time.strftime("%H %M")
                saat1=cikisZamani[0]
                saat2=cikisZamani[1]
                saat=saat1+saat2

                saat=int(saat)


                dakika1=cikisZamani[3]
                dakika2=cikisZamani[4]
                dakika=dakika1+dakika2
                dakika=int(dakika)

                inttime=(c*60)+d
                outtime=(saat*60)+dakika
                toplam=(outtime-inttime)/60

                if 0<=toplam<1.99:    #0<=toplam<1.99
                    self.fiyati.setText('10 ')
                elif 1<=toplam<3.99 :
                    self.fiyati.setText('15 ')
                elif 3<=toplam<6.99:
                    self.fiyati.setText('24 ')
                elif 6<=toplam<12.99:
                    self.fiyati.setText('30 ')
                elif 12<=toplam<24.99:
                    self.fiyati.setText('40 ') #buraya kadar zamani hisapliyor

                if (veriler['citys']['yukseklikleri']>1.9): #burada eger yuksek 1.9dan buyuk ise fiyati %20 artirir
                    b=float(self.fiyati.text())
                    artma=b+((b*20)/100)
                    self.fiyati.setText(str(artma))
                    acmak.close()

                ihras=veriler['citys']['yeri']  #burada cikan arabalarin yeri bos biraksin
                if (yerler[ihras]=='full'):
                    yerler[ihras]='free'
                print(yerler)
                break
            #else:
                #self.plakasi.setStyleSheet("background-color: rgb(250, 10, 25);")   # araba otoparkta degil ise bu mesaj yapsin ama olmadi
                #self.plakasi.setText('Boyle bir araba yok otoparkta !!!')
                #self.cikisSaati.setText("")
                #time.sleep(3)
                #exit()











uygulama = QApplication([])
pencere = Otopark_Otomasyonu()
pencere.show()
uygulama.exec_()
