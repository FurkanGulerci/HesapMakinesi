while True:
    Bir_Sayı_Giriniz = float(input("Bir Sayı Giriniz:"))
    İkinci_Sayıyı_Giriniz = float(input("İkinci Sayıyı Giriniz:"))

    print("\n1. Toplama(+)\n2. Çıkarma(-)\n3. Çarpma(*)\n4. Bölme(/)\n5. Yüzde(%)\n")
    islem = input("Hangi İşlemi Yapmak İstiyorsunuz: ")


   #Toplama
    if islem == "1" or islem == "+":
        print("\nToplama Sonucu: ", Bir_Sayı_Giriniz + İkinci_Sayıyı_Giriniz)
    #Çıkarma
    elif islem == "2" or islem == "-":
        print("\nÇıkarma Sonucu: ", Bir_Sayı_Giriniz - İkinci_Sayıyı_Giriniz)
    #Çarpma
    elif islem == "3" or islem == "*":
        print("\nÇarpma Sonucu: ", Bir_Sayı_Giriniz * İkinci_Sayıyı_Giriniz)
    #Bölme
    elif islem == "4" or islem == "/":
        if İkinci_Sayıyı_Giriniz == 0:
            print("\n0'a Bölme İşlemi Yapılamaz.")
        else:
            print("\nBölme Sonucu: ", Bir_Sayı_Giriniz / İkinci_Sayıyı_Giriniz)
    #Yüzde
    elif islem == "5" or islem == "%":
        print("\nYüzde Sonucu: ", Bir_Sayı_Giriniz % İkinci_Sayıyı_Giriniz)
    else:
        print("\nGeçersiz İşlem")
    

    devam = input("\nBaşka Bir İşlem Yapmak İster Misiniz? (Evet/Hayır): ")
    if devam.lower() != "evet":
        print("\nProgram Sonlandırıldı.")
        break
