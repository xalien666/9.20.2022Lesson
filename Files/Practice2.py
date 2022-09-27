file = open("test1.txt","r") #

oxu_fayl1= file.read()

print("1. Dəfə oxuyuruq\n",oxu_fayl1,sep="")

oxu_fayl2=file.read()

print("2. Dəfə oxuyuruq\n",oxu_fayl2,sep="")

file.close()