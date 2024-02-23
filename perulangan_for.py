#i bisa di ganti dengan variabel lain seperti: angka,j.dll
for i in range(7):
    print("python")
print("==================")
#i=0  --> print("python")
#i=1  --> print("python")
#i=3  --> print("python")
#i=4  --> print("python")
#i=5  --> print("python")
#i=6  --> print("python")
print("==========")
for i in range(21): #start dari angka 0
    print(i)

for i in range(3, 21): #untuk start dari angka 3
    print(i, end=" ") #end untuk menampilkan angka ke samping
print("==========")
jumlah=0
for angka in range(5, 21):
    print(angka, end=" ")
    jumlah=jumlah+angka

print("jumlah=",jumlah)

print()

#==========================
#jumlah=0
#angka=5    --> print(5)    --> jumlah= 0 + 5 = 5
#angka=6    --> print(6)    --> jumlah= 5 + 6 = 11
#angka=7    --> print(7)    --> jumlah= 11 + 7 = 18
#.....sampai
#angka=20    --> print(20)    --> jumlah= 180 + 20 = 200

for i in range(1, 101):
    print("Perulanngan ke-",i)

print()

for angka in range(1, 13):
    print(angka, end=" ")
    
print()

for genap in range(1, 21):
    if (genap %2==0):
        print(genap)

print()

for ganjil in range(1, 21):
    if (ganjil %2==1):
        print(ganjil)