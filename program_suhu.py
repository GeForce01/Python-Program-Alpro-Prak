c=float(input("masukkan suhu:"))

reamur=4/5*c
fahrenheit=(9/5*c)+32

pilih=input("masukkan pilihan anda (reamur/fahrenheit):")

if(pilih=="reamur"):
    print("suhunya adalah:",reamur)
else:
    print("suhunya adalah:",fahrenheit)