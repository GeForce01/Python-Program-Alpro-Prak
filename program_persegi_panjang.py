panjang=float(input("masukkan panjang:"))
lebar=float(input("masukkan lebar:"))

keliling=2*(panjang+lebar)
luas=panjang*lebar

pilih=input("masukkan pilihan anda(keliling/luas):")

if(pilih=="keliling"):
     print("keliling persegi panjang adalah:",keliling)

else:
    print("luas persegi panjang adalah:",luas)