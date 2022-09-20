print(
      """
      Faktorial tapan proqram
      
      Proqramdan cixmaq istedikde "q" ya basin
      """
      )

while True:
    
    reqem = input("reqemi daxil edin")
    
    if reqem =="q":
        print("Proqramdan cixilir")
        break
    
    reqem = int(reqem)
    
    fakt = 1
    
    for i in range(2,reqem+1):
        
        fakt *=i
        
    print("Faktorial:",fakt)
    