
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
