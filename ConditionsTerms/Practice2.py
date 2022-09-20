print("""
      Istifadeci girisi\n
      """)

nick = "AliaghaSahibjanov"
pas = "123456"

nickname = input("Istifadeci adini daxil edin")
password = input("Sifreni daxil edin")

if(nickname != nick and password ==pas):
    print("Istifadeci adiniz yalnisdir")

elif(nickname == nick and password !=pas):
    print("Sifre yalnisdir")

elif(nickname != nick and password !=pas):
    print("Istifadeci adi ve sifre yalnisdir")
else:
    print("Giris ugurludur!")