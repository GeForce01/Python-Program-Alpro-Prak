nilai_un=float(input("masukkan nilai un anda:"))
gaji_ortu=float(input("masukkan gaji ortu anda:"))

if(nilai_un>=85 and gaji_ortu<2000000):
    status="anda mendapatkan beasiswa"
else:
    status="anda tidak mendapatkan beasiswa"

print(status)