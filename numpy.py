import numpy as np
dizi=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)
print(dizi.shape) # dizi boyutu
dizi2=dizi.reshape(3,5) # 3 satir 5 sütunluk bir matris oluşturma
print(dizi2)
print("şekil: ",dizi2.shape)
print("Boyut: ",dizi2.ndim)
print("Tipi: ",dizi2.dtype.name)
#2D array
dizi2D=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(dizi2D)
# sıfırlardan oluşmuş dizi
sifir_dizi=np.zeros((3,4))
print(sifir_dizi)
# birlerden oluşmuş dizi
bir_dizi=np.ones((3,4))
print(bir_dizi)
#arange
dizi_aralik=np.arange(5,105,5)
print(dizi_aralik)

#Linspace(x,y,basamak) x ve y arasındaki değerleri bsamak kadar ayırır.
dizi_bosluk=np.linspace(5,105,5)
print(dizi_bosluk)

#floatArray oluşturma
float_array=np.float32([[1,2],[3,4]])
print(float_array)

#Matematiksel işlemler
array_1=np.array([1,2,3,4])
array_2=np.array([5,6,7,8])
print(array_1+array_2)
print(array_1-array_2)
print(array_1**2)
#dizi elemanlarını toplama
print(np.sum(array_1))
#dizi ortalamsını hesaplama
print(np.mean(array_1))
# max veya min değer hesaplamma
print(np.max(array_1))
#medyan bulma
print(np.median(array_1))
#rastgele sayı oluşturma [0,1] arasında sürekli uniform
rastgele_sayi=np.random.random((3,3))
print(rastgele_sayi)
#indekslere ulaşma
array=np.array([[1,2,3,4],[9,10,11,21]])
print(array[1,1])
#1. sütun ve tüm sayılar
print("2. sütun ve tüm sayılar",array[:,1])
#satır 2, sütun 1 2 3
print("2. satır için ilk 3 eleman",array[1,1:4])
dizi2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
vektor=dizi2d.ravel()
print(vektor)
max_sayinin_indexi= dizi2d.argmax()
print(max_sayinin_indexi)
