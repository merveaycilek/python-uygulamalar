#1) Klavyeden girilen iki adet sayının toplamını ekrana yazdıran programın python kodlarını yazınız.
sayi1 = int(input('Sayı1: '))
sayi2 = int(input('Sayı2: '))
print(sayi1 + sayi2)


#2) Klavyeden girilen 5 adet sayının toplamının çift mi tek mi olduğunu yazdıran programın python kodlarını yazınız.
sayi1 = int(input('Sayı1: '))
sayi2 = int(input('Sayı2: '))
sayi3 = int(input('Sayı3: '))
sayi4 = int(input('Sayı4: '))
sayi5 = int(input('Sayı5: '))
a = (sayi1 + sayi2 + sayi3 + sayi4 + sayi5)
if a % 2 == 0:
  print(f'sayı çift sayıdır')
else:
  print(f'sayı tek sayıdır')


#3) Kullanıcıdan doğum yılı bilgisi alınarak kaç yaşında olduğunu söyleyen programın python kodlarını yazınız
yil = int(input('Hangi Yıldayız: '))
dogum_yili = int(input('Doğum Yılı: '))
a = (yil - dogum_yili)
print(a)

#4) Kullanıcının kilo bilgisi alınarak kilo 50 ve altında ise zayıf, 50-80 arası ideal, 80 ve üstü ise kilolu şeklinde ekranda yazdırınız
kilo = int(input('Kilonuz: '))
if kilo < 50:
   print(f'zayıf')
if 50 < kilo < 80:
   print(f'ideal')  
if kilo >= 80:
   print(f'kilolu')    


#5) Haftanın gün bilgisini alıp cumartesi ve pazarsa tatil değilse çalışıyorsun şeklinde ekrana uyarı veren programın python kodlarını yazınız
gün = input('Haftanın hangi günü: ')
if gün == "cumartesi" or gün == "pazar":
   print('çalışmıyorsun')
else:
   print('çalışıyorsun')      


#6) Kullanıcının yaş bilgisi alınıp 12 yaşından küçükse çocuk 12-28 yaş arası ise genç, 28-40 yaş arası ise orta yaşlı 40 yaştan büyükse yaşlı
yas = int(input('Yaş bilginizi giriniz: '))
if yas < 12:
   print ("çocuk")
if 12 < yas < 28:
   print ("genç")
if 28< yas < 40:
   print ("orta yaş")
if yas >= 40:
   print ("yaşlı")



#Girilen 5 sayıdan en büyüğünü gösteren programın python kodlarını yazınız.
sayi1 = int(input('Sayı1: '))
sayi2 = int(input('Sayı2: '))
sayi3 = int(input('Sayı3: '))
sayi4 = int(input('Sayı4: '))
sayi5 = int(input('Sayı5: '))
if sayi1>sayi2 or sayi1 > sayi3 or sayi1>sayi4 or sayi1>sayi5:
 3 print ("Sayı 1 en büyük sayıdır.")
elif  sayi2>sayi3 or sayi2>sayi4 or sayi2>sayi5:
  print ("Sayı 2 en büyük sayıdır.")  
elif sayi3>sayi4 or sayi3>sayi5:
  print ("Sayı 3 en büyük sayıdır.") 
elif sayi4>sayi5:
  print ("Sayı 4 en büyük sayıdır.") 
else:
   print ("en büyük sayı Sayı 5 tir.")


#Cümledeki harf sayısını bulan python kodunu yazdırın.
cumle = input("cümleyi gir: ")
print("cümledeki harf sayısı" , len(cumle))


#Kullanıcı adı ve parolayla giriş yapılacak bir uygulama kodlayın.
kullanici_adi = "merve"
sifre = "12345"
while True:
   kullanici_adi = input("kullanıcı adı: ")
   sifre = input("şifreniz: ")
   if kullanici_adi == "merve" and sifre == "12345":
      print("giriş başarılı.")
      break
   else:
      print("parola veya şifre yanlış.")


#yaşı 65 ile karşılaştıran yaş 65 ten büyük ya da eşitse yaşlı nüfusa 1 aksi taktirde diğerlerine 1 ekleyen if else ifadesi yazın
a= "yaşlı nüfus"
b= "genç nüfus"

yas = int(input("Yaşınızı giriniz: "))
if yas >= 65:
   print("yaşlı nüfusa bir eklendi.")
else:
   print("genç nüfusa bir eklendi.")   


#döngü kullanın ve 5 adımlık aralıklarla 4 ile 50 arasındaki sayıları yazdırın
x=4 
while x < 50:
   print(x)
   x = x + 5
print("bitti")
















