print("""
      ...........................
       Kalkulyator by Sahibcanov
       
       Prosesler:
           
           1-Toplama
           2-Cixma
           3-Vurma
           4-Bolme
      ...........................
      """)
    
a=int(input("Ilk reqemi daxil ediniz"))
b=int(input("Ilk reqemi daxil ediniz"))

proses = int(input("Icra etmek istediyiniz prosesin kodunu daxil edin"))

if(proses==1):
    print("{} ile {} toplami {}-a beraberdir".format(a,b,a+b))
elif(proses==2):
    print("{} ile {} ciximi {}-a beraberdir".format(a,b,a-b))
elif(proses==3):
    print("{} ile {} vurulmasi {}-a beraberdir".format(a,b,a*b))
elif(proses==4):
    print("{} ile {} bolmesi {}-a beraberdir".format(a,b,a/b))
else:
    print("Bele bir proses kodu yoxdur")