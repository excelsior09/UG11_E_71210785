print ("=======Program Manipulasi String=======")
print ("Pilihan Menu")
print ("1. Hitung kata")
print ("2. cek kata")
print ("3. ubah kata")

a = int(input("Pilihan anda : "))
b = input("Masukan sebuah kalimat/kata : ")
kalimat = b.lower()
if a == 1:
    c = input("Masukan kata yang ingin dihitung : ").lower()
    ab = kalimat.count(c)

    print ("Terdapat sebanyak", ab, "kata", c, "didalam string")
elif a == 2:
    c = input("Masukan kata yang ingin di cek : ")
    ac = c.upper()
    hasil = kalimat.replace(c, ac)
    if ac not in kalimat:
        print ("Kata", c, "tidak terdapat di dalam string")
        print ("String diubah menjadi : ")
        print (hasil, c)
    else:
        print ("Kata", c, "terdapat di dalam string")
        print ("String diubah menjadi : ")
        print (hasil)
    
elif a == 3:
    c = input("Masukan kata yang ingin diubah : ")
    d = input("Masukan kata pengganti : ")

    print ("Anda akan mengubah kata", c, "menjadi", d, "sebanyak 1x")
    cd = input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")
    if cd == "yes":
        e = int(input("Masukan jumlah total penggantian : "))
        print ("String berhasil diubah menjadi : ")

        f = kalimat.replace(c, d, e)
        print (f)
    elif cd == "no":
        e = 1
        print ("String berhasil diubah menjadi : ")

        f = kalimat.replace(c, d, e)
        print (f)