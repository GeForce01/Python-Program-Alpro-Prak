nama=(input("Masukkan Nama Anda = "))
list=["A","a","I","i","E","e","O","o"]
for i in list:
    if(i=="A" or i=="a"):
        nama=nama.replace(i,"@") #replace untuk mennganti huruf
    elif(i=="I" or i=="i"):
        nama=nama.replace(i,"1")
    elif(i=="E" or i=="e"):
        nama=nama.replace(i,"3")
    elif(i=="O" or i=="o"):
        nama=nama.replace(i,"0")

print("Nama Alay Anda Adalah =",nama)
#menggunakan replace
nama=(input("Masukkan Universitas Anda = "))
list=["A","a","I","i","E","e","O","o"]
for i in list:
    if(i=="A" or i=="a"):
        nama=nama.replace(i,"@")
    elif(i=="I" or i=="i"):
        nama=nama.replace(i,"1")
    elif(i=="E" or i=="e"):
        nama=nama.replace(i,"3")
    elif(i=="O" or i=="o"):
        nama=nama.replace(i,"0")

print("Universitas Alay Anda Adalah =",nama)

#tanpa replace 
nama=input("Ketik Nama Anda = ")

nama_alay=" "
for huruf in nama:
    if(huruf in ("a","A")):
        nama_alay+="@"
    elif(huruf in ("I","i")):
        nama_alay+="1"
    elif(huruf in ("E","e")):
        nama_alay+="3"
    elif huruf in("O","o"):
        nama_alay+="0"
    else:
        nama_alay+=huruf
print("Nama Alay Anda Adalah = ",nama_alay)    

nama=input("Ketik Universitas Anda = ")

nama_alay=" "
for huruf in nama:
    if(huruf in ("a","A")):
        nama_alay+="@"
    elif(huruf in ("I","i")):
        nama_alay+="1"
    elif(huruf in ("E","e")):
        nama_alay+="3"
    elif huruf in("O","o"):
        nama_alay+="0"
    else:
        nama_alay+=huruf
print("Universitas Alay Anda Adalah = ",nama_alay)  