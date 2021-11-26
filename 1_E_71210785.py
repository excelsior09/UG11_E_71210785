print ("Menu Program Yang Tersedia")
print ("1. pangkatkan angka")
print ("2. akarkan angka")

n = float(input("Masukan pilihan yang "))
if n == 1:
    print ("Masukan angka yang ingin di pangkatkan")
    a = float(input("Angka : "))
    print ("ingin memodifikasi akar ? (yes/no)")
    z = str(input(": "))
    if z == "yes":
        b = float(input("Masukan nilai pangkat : "))
        ab = a ** b
        print ("Hasil dari ", a,"^",b, "=",ab)
    elif z == "no":
        ab = a ** 2
        print ("Hasil dari ", a,"^ 2", "=",ab)
    else :
        print ("sistem error")
elif n == 2:
    print ("Masukan angka yang ingin di akar")
    a = float(input("Angka : "))
    print ("ingin memodifikasi akar ? (yes/no)")
    z = str(input(": "))
    if z == "yes":
        b = float(input("Masukan nilai akar : "))
        ab = a ** (1.0/b)
        print ("Hasil akar pangkat", b,"dari",a, "=",round(ab,2))
    elif z == "no":
        ab = a ** (1.0/2)
        print ("Hasil akar pangkat 2 dari",a, "=",round(ab,2))
    else:
        print ("sistem error")
else:
    print("Menu tidak ada")