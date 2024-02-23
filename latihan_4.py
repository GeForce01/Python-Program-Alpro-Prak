print("===Menentukan Jenis Segitiga===")
s1=float(input("Masukkan Sisi 1 = "))
s2=float(input("Masukkan Sisi 2 = "))
s3=float(input("Masukkan sisi 3 = "))

if(s1==s2==s3):
    print("Ini Adalah Segitiga Sama Sisi")
    print("===Terima Kasih===")

elif(s1==s2 or s1==s3 or s2==s3):
    print("Ini Adalah Sigitiga Sama Kaki")
    print("========Terima Kasih========")

else:
    print("Ini Adalah Segitiga Sembarang")
    print("========Terima Kasih========")