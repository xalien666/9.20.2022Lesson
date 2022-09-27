def ebob(a,b):
    
    if b == 0:
        return a
    else:
        return ebob(b,a%b)
    
a = int(input("Birinci ededi girin"))
b = int(input("Ikinci ededi girin"))

print(ebob(a, b))



