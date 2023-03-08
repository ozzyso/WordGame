isim = input("İsim giriniz: ")
print("Merhaba " + isim + " oyuna başalayalım.")
gizli_kelime = "marangoz"
cevaplar = ""
can = 10

while can > 0 :
    kalan_harf = 0
    for harf in gizli_kelime:  # harf gizli_kelime'nin herbir karakteri
        if harf in cevaplar:
            print(harf, end="")
        else:
            print("*", end="")
            kalan_harf += 1
    print("")        #alt satıra almak için end="" de aynı.
    if kalan_harf == 0:
        print("Tebrikler!!! Oyunu Kazandınız!")
        break
    print("Oyundan çıkmak için 1'e basın")
    cevap = input("Bir harf girin: ")
    #cevap = cevap [0] eğer kullanıcı kelime girerse ama bu sefer boşlukda error veriyor.
    if cevap == "1":
        print(f"{isim} oyundan çıktı.")
        break
    if  cevap not in cevaplar:
        cevaplar += cevap
        if cevap not in gizli_kelime:
            can -= 1
            print("Yanlış cevap!")
            print(f"Kalan can sayısı: {can}")
            if can == 0:
               print("Oyun bitti!")
    else:
        print(f"({cevap})=> bu cevap daha önce verildi. Başka bir harf giriniz.")