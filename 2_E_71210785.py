def huruf_tengah(kata):
    a = len(kata)//2

    if (len(kata) % 2 == 0) and ((len(kata) / 2) % 2 == 0):
        return kata[(a) // 2 : ((a) // 2) * -1]
    elif (len(kata) % 2 == 0) and ((len(kata) / 2) % 2 != 0):
        return kata[((a) // 2) + 1 : (((a) // 2) + 1) * -1]
    else:
        return kata[(((a) + 1) // 2) : (((a) + 1) // 2) * -1]

kata = str(input("Masukan kata : "))
print ("Harus tengah pada kata", kata, "adalah", huruf_tengah(kata))