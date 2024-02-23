print("Menghitung Diskon Harga Produk")
print("====Selamat Datang Di Punk Kank Store====") 
j=input("Jenis Produk = ")
jp=int(input("Jumlah Produk = "))
hp=float(input("Harga Produk = Rp."))

h=jp*hp
print("Bayar = Rp.",h)

if(h>500000):
    print("Anda Mendapatkan Diskon 20%")
    hd=h*0.2
    tb=h-hd
    print("Total Bayar = Rp.",tb)
    print("===Selamat Berbelanja Dan Terima Kasih===")

elif(h>300000):
    print("Anda Mendapatkan Diskon 10%")
    hd=h*0.1
    tb=h-hd
    print("Total Bayar = Rp.",tb)
    print("===Selamat Berbelanja Dan Terima Kasih===")

elif(h>150000):
    print("Anda Mendapatkan Diskon 5%")
    hd=h*0.05
    tb=h-hd
    print("Total Bayar = Rp.",tb)
    print("===Selamat Berbelanja Dan Terima Kasih===")

else:
    print("Anda Tidak Mendapatkan Diskon ")
    print("Total Bayar = Rp.",h)
    print("===Selamat Berbelanja Dan Terima Kasih===")

