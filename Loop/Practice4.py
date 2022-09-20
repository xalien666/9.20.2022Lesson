print(
      """
      Bankomat
      
      Proqramdan cixmaq istedikde "q" ya basin
      
      Proses:
      1-Pul sorgula
      2-Pul yatirma
      3-Pul cekme
      """
      )
hesabdakipul = 1000
while True:
    proses = input("Prosesi daxil edin")
    
    if (proses =="q"):
        print("Proqramdan cixilir")
        break
    
    elif (proses == "1"):
        print(hesabdakipul)
    
    elif (proses=="2"):
        mebleg = int(input("Yatirmag istediyiniz meblegi girin"))
    
        hesabdakipul = hesabdakipul + mebleg
        print(hesabdakipul)
        
    elif (proses=="3"):
        mebleg = int(input("Yatirmag istediyiniz meblegi girin"))
        hesabdakipul=hesabdakipul-mebleg
        print(hesabdakipul)
