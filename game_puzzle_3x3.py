import os
import random
from random import shuffle
# Source code python Game ini Milik 
# Nama = MUHAMMAD ZYDANE ARROSYID ( NPM = 5200411118 )
# Kelas = B , Kelompok praktikum = III
# Dasar Code / Main Code diambil dari code petani jagung domba serigala :) Terima kasih pak :)
def random_angka(List_Variable): # Hardest Part maybe ?
    random.shuffle(List_Variable)

def tampil_gambar(List_Variable): # bagian menampilkan list puzzle dalam bentuk 3x3 
    print("GAME PUZZLE 3x3 ! \n")
    print("""
=============    
| {} | {} | {} |
=============
| {} | {} | {} |
=============
| {} | {} | {} |
=============""".format(*List_Variable)) #done for now at lest

def change(List_Variable): # memindahkan list ~ ok i found another problem, how to limit it to the left of "_" or right or top of it, fuck my life 
    angka = input("Masukan Angka yang ingin di pindah kan : ")

    if List_Variable.index("_") == 0:
        if angka == List_Variable[1]:
            List_Variable[1], List_Variable[0] = List_Variable[0], List_Variable[1]
        elif angka == List_Variable[3]:
            List_Variable[3], List_Variable[0] = List_Variable[0], List_Variable[3]
        else:
            print("Angka tidak bisa di pindahkan !")

    elif List_Variable.index("_") == 1:
        if angka == List_Variable[0]:
            List_Variable[0], List_Variable[1] = List_Variable[1], List_Variable[0]
        elif angka == List_Variable[2]:
            List_Variable[2], List_Variable[1] = List_Variable[1], List_Variable[2]
        elif angka == List_Variable[4]:
            List_Variable[4], List_Variable[1] = List_Variable[1], List_Variable[4]
        else:
            print("Angka tidak bisa di pindahkan !")

    elif List_Variable.index("_") == 2:
        if angka == List_Variable[1]:
            List_Variable[1], List_Variable[2] = List_Variable[2], List_Variable[1]
        elif angka == List_Variable[5]:
            List_Variable[5], List_Variable[2] = List_Variable[2], List_Variable[5]
        else:
            print("Angka tidak bisa di pindahkan !")
    elif List_Variable.index("_") == 3:
        if angka == List_Variable[0]:
            List_Variable[0], List_Variable[3] = List_Variable[3], List_Variable[0]
        elif angka == List_Variable[4]:
            List_Variable[4], List_Variable[3] = List_Variable[3], List_Variable[4]
        elif angka == List_Variable[6]:
            List_Variable[6], List_Variable[3] = List_Variable[3], List_Variable[6]
        else:
            print("Angka tidak bisa di pindahkan !")
    elif List_Variable.index("_") == 4:
        if angka == List_Variable[1]:
            List_Variable[1], List_Variable[4] = List_Variable[4], List_Variable[1]
        elif angka == List_Variable[3]:
            List_Variable[3], List_Variable[4] = List_Variable[4], List_Variable[3]
        elif angka == List_Variable[5]:
            List_Variable[5], List_Variable[4] = List_Variable[4], List_Variable[5]
        elif angka == List_Variable[7]:
            List_Variable[7], List_Variable[4] = List_Variable[4], List_Variable[7]
        else:
            print("Angka tidak bisa di pindahkan !")
    elif List_Variable.index("_") == 5:
        if angka == List_Variable[2]:
            List_Variable[2], List_Variable[5] = List_Variable[5], List_Variable[2]
        elif angka == List_Variable[4]:
            List_Variable[4], List_Variable[5] = List_Variable[5], List_Variable[4]
        elif angka == List_Variable[8]:
            List_Variable[8], List_Variable[5] = List_Variable[5], List_Variable[8]
        else:
            print("Angka tidak bisa di pindahkan !")
    elif List_Variable.index("_") == 6:
        if angka == List_Variable[3]:
            List_Variable[3], List_Variable[6] = List_Variable[6], List_Variable[3]
        elif angka == List_Variable[7]:
            List_Variable[7], List_Variable[6] = List_Variable[6], List_Variable[7]
        else:
            print("Angka tidak bisa di pindahkan !")
    elif List_Variable.index("_") == 7:
        if angka == List_Variable[4]:
            List_Variable[4], List_Variable[7] = List_Variable[7], List_Variable[4]
        elif angka == List_Variable[6]:
            List_Variable[6], List_Variable[7] = List_Variable[7], List_Variable[6]
        elif angka == List_Variable[8]:
            List_Variable[8], List_Variable[7] = List_Variable[7], List_Variable[8]
        else:
            print("Angka tidak bisa di pindahkan !")
    elif List_Variable.index("_") == 8:
        if angka == List_Variable[5]:
            List_Variable[5], List_Variable[8] = List_Variable[8], List_Variable[5]
        elif angka == List_Variable[7]:
            List_Variable[7], List_Variable[8] = List_Variable[8], List_Variable[7]
        else:
            print("Angka tidak bisa di pindahkan !")
    else:
        print("WTF HOW ?!?!?!")

def cek_selesai(List_Variable): # check kalau index list sama ( karena jika hanya menggunakan 1 list maka yang di permainkan adalah index nya)
    if List_Variable == menang:
        print("Selamat Anda Berhasil menyelesaikan Puzzle 3x3 ini ! dengan Total Score = ",score)
        selesai = True
        return selesai
    else:
        selesai = False
        return selesai

# Program Utama Port From game petani jagung domba serigala ~
os.system("cls")
List_Variable = ["1","2","3","4","5","6","7","8","_"]
menang = ["1","2","3","4","5","6","7","8","_"]
score = 0
selesai = False     #False jika permainan belum berakhir. True jika permainan berakhir
main_lagi = 'Y'     #'Y' jika user ingin bermain lagi. 'T' jika user tidak ingin bermain lagi

random_angka(List_Variable)
tampil_gambar(List_Variable) # Need Change

while (main_lagi.upper() == 'Y'):
    change(List_Variable) # Need Change !
    score = score + 1
    input()
    os.system("cls")

    tampil_gambar(List_Variable) # need change

    selesai = cek_selesai(List_Variable) # need change

    #jika selesai = True, tanya apakah mau main lagi atau tidak , yup ter port dari tugas sblm nya
    if (selesai == True):
        main_lagi = input("\nMain lagi (Y/T)? ")
        random_angka(List_Variable)
        #Check if there some odd  
        if ( main_lagi == "y" or main_lagi == "Y"):
            selesai = False
            score = score - score
            os.system("cls")
            tampil_gambar(List_Variable) # need change