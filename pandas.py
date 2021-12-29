import pandas as pd
#sözlük oluştur
dictionary={"isim":["Ali","Ömer","Faruk","Doğan"],
            "yas":[18,19,20,21],
            "maas":[3000,4000,5000,6000]}
veri=pd.DataFrame(dictionary)
print(veri)
print(veri.columns)
# veri bilgisi
print(veri.info())
#istatistiksel özellikler
print(veri.describe())
#yas sütunu
print(veri["yas"])
#sütun eklemek
veri["sehir"]=["İstanbul","Ankara","Aydın","Antalya"]
print(veri)
#yas sütunu 
print(veri.loc[:,"yas"])
#yas sütunu ve ilk 3 satırı
print(veri.loc[:2,"yas"])
#yas ve sehir arası sütunu 3 satır
print(veri.loc[:2,"yas":"sehir"])
#yas ve sehir sütunların ilk 3 satırı
print(veri.loc[:3,["yas","sehir"]])
#satırları sondan yazdır
print(veri.loc[::-1,:])
# yas sütununu iloc(index) ile yazmak
print(veri.iloc[:,1])
# ilk 3 satır ;yas ve isim
print(veri.iloc[0:2,[0,1]])
#filtreleme
dictionary2={"isim":["Ali","Ömer","Faruk","Doğan"],
            "yas":[18,19,20,21],
            "sehir":["İstanbul","Ankara","Ankara","Antalya"]}
veri2=pd.DataFrame(dictionary2)
#ilk önce yaşa göre bir filtre oluşturalım bu filtre
#yas>20
filtre0=veri.yas>20
filtrelenmis_data=veri[filtre0]
print(filtrelenmis_data)
#ortalama yas
ortalama_yas=veri.yas.mean()
veri2["yas_grubu"]=["küçük" if ortalama_yas>i else "büyük" for i in veri.yas]
#üst satırda yas_grubu diye bir sütun oluşturuyoruz. 
#yas_grubu sütununa eğer yas ortalamasından düşükse küçük büyüykse büyük yazdırıryoruz.
print(veri2)
#birlesştirme
sozluk1={"isim":["Ali","Ömer","Faruk"],
            "yas":[18,19,20],
            "sehir":["İstanbul","Ankara","Ankara"]}
veri_1=pd.DataFrame(sozluk1)

sozluk2={"isim":["Ahmet","Hakan","Furkan"],
            "yas":[28,29,25],
            "sehir":["Malatya","Adıyaman","İzmir"]}
veri_2=pd.DataFrame(sozluk2)
#dikey birleştirme
veri_dikey=pd.concat([veri_1,veri_2],axis=0);
print(veri_dikey)
