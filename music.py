#encoding = UTF-8
#@coder_m.yagiz or @codermyagiz tüm sosyal platformlar

import time
import winsound #şarkıları oynatmak için

print("Kendinize özel şarkı yazma uygulamasına hoş geldiniz!")

isim = input("İsminiz nedir:")
yas = int(input("Yaşınız nedir:"))
secim = int(input("1. Gesi Bağları\n 2. Mihriban\n 3.Girişimcilere Özel \n"))

if secim == 1:
	print("Gesi bağları seçildi.")
	print("Kendinize özel şarkınız hazırlanıyor. Lütfen bekleyiniz...")
	time.sleep(2)
	winsound.PlaySound('gesi.wav', winsound.SND_ASYNC) #Şarkının arka planda çalmasını sağlar.
    print("Gesi bağlarından dolanıyorum\nYitirdim {} amman aranıyorum\nYitirdim {} amman aranıyorum".format(isim,isim))

if secim == 2:
	print("Mihriban seçildi.")
	sac = input("Saç renginiz nedir?")
	print("Kendinize özel şarkınız hazırlanıyor. Lütfen bekleyiniz...")
	time.sleep(2)
	winsound.PlaySound('mihirban.wav', winsound.SND_ASYNC)
    print("{} saçlarına deli gönlümü\nBağlamışım çözülmüyor\n{}, {}\nAyrılıktan zor belleme ölümü,\nölümü\nGörmeyince sezilmiyor {}".format(sac,isim,isim,isim))

if secim == 3:
	print("Girişimciliğinize özel şarkınız seçildi.")
	print("Girişimciliğinize özel şarkınız hazırlanıyor. Lütfen bekleyiniz...")
	time.sleep(2)
    print("Aklını ferah tut, arkana bakma\nSöylenenlere aldırma, asla pes etme {}\nCesaretini hemen topla\nHadi düşünsene {}".format(isim,isim))

    #Not: Girişimciliğinize özel şarkısındaki bazı bölümler Esra Karaduman'dan alıntıdır.
    #Not: "Efsane Sensin" şarkısından alınıp bazı bölümler değiştirilmiştir.
