"""
a=open("informasiyalar.txt","a")

a.write("\nAliagha Sahibjanov")

a.close()

a=open("informasiyalar.txt","a")

a.write("\nHesen Sahibjanov")

a.close()


with open("informasiyalar.txt", "r") as a:
    
    for i in a:
        print(i, end="")

"""

fayl = open("test1.txt","w")
fayl.write("Ali SHBCN")
fayl.close()

fayl = open("test1.txt","a")
fayl.write("\nHesen SHBCN")
fayl.close()

fayl = open("test1.txt","a")
fayl.write("\nFidan SHBCN")
fayl.close()