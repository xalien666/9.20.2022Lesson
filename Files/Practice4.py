with open("test1.txt","r") as fayl:
    print("Kursorumuz bu baytdadir",fayl.tell())
    
    fayl.seek(34)
    
    print("Kursorumuz bu baytdadir",fayl.tell())
    
    oxu_fayl = fayl.read()
    
    print("Faylin icindeki deyer: ", oxu_fayl)