import random #library(add on atau tambahan)
acak=random.randint(1, 10)
print("Komputer Sudah Mengacak Bilangan Dari 1 s.d. 10")
angka=int(input("Tebakan Anda: "))

angka=0
while(angka != acak):
    print("Tebakan Anda Salah! Coba Lagi.")
    angka=int(input("Tebakan Anda: "))

print("Tebakan Anda Benar")
print("Angkanya Adalah",acak)

