name='berfin'
surname='özkan'
age='20'
mesaj='Merhaba'
print(mesaj+' ben '+ name +' '+ surname+' '+ age+' yasindayim')
print('bilgisayar müdendisliği 2. sinif ogrencisiyim')
print(type(name))
a=15.3
b=3.0
sonuc=a/b
print(sonuc)
print(type(sonuc))


yazi='kodlama'
print(yazi)
print(yazi[3])
print(yazi[4:7])
print(yazi[3:])
print(yazi*3)
print(yazi+' sevilmez mi')

liste1=[20,100,6,'kar','berfin']
liste2=[1002,'c',40,'selam']
print(liste1)
print(liste1[0])
print(liste1[1:3])
print(liste2[3:])
print(liste2*2)
print(liste1+liste2)

list=[1,8,6,4,2]
length=len(list)
print('liste uzunlugu:',length)
list.sort()
list.append(10)
list.remove(8)
print('güncel liste:',list)
print('listenin 4. elemani:',list[3])
list.clear()
print('listeyi bosalttık:',list)