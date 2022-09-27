"""
def sade_eded(eded):
    if(eded==1):
        return False
    elif(eded==2):
        return False
    else:
        for i in range(2,eded):
            if(eded%i==0):
                return False
        
        return True
    
while True:
    eded = input("Ededi girin")
    
    if (eded=="q"):
        break
    else:
        eded=int(eded)
        
        if (sade_eded(eded)):
            
            print("Daxil etdiyiniz eded  {} sade ededdir".format(eded))
        
        else:
            print("Daxil etdiyiniz eded  {} sade eded deil".format(eded))

"""

def tam_bolunenler(eded):
    bolunenler = list()
    
    for i in range(2,eded):
        
        if(eded%i==0):
            bolunenler.append(i)
    return bolunenler

while True:
    eded = input("Tam bolunenler Ededi girin")
    
    if (eded=="q"):
        break
    else:
        eded=int(eded)
        
        a = tam_bolunenler(eded)
        
        print("Ededin tam bolunenleri",a)
        
        

def ebob(m,n):
    
    if n == 0:
        return m
    else:
        return ebob(n,m%n)
    
    m = int(input("Ebob Birinci ededi girin"))
    n = int(input("Ebob Ikinci ededi girin"))

    print(ebob(m, n))



