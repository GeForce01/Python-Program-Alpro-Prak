#================================================================================
#Program Petani-Domba-Jagung-Serigala
#Pemain harus memindahkan petani, domba, jagung, dan serigala ke seberang sungai 
#menggunakan perahu yang hanya dapat memuat petani dan satu bawaan
#================================================================================
#Kode Program ini Milik : MUHAMMAD ZYDANE ARROSYID ( 5200411118 ) KELAS : B , KELOMPOK PRAKTIK : III
#import library
import os

#sub program (prosedur dan fungsi)
def tampil_gambar(list_kiri, list_kanan):
    #print("silakan isi kode program untuk prosedur tampil_gambar()")
    if ("P" in list_kiri):
        print(*list_kiri," "*28,*list_kanan, sep=' ')
        print("="*10,perahu_di_kiri,"="*10)
    else:
        print(*list_kiri," "*28,*list_kanan, sep=' ')
        print("="*10,perahu_di_kanan,"="*10)

def menyeberang(list_kiri, list_kanan):
    #print("silakan isi kode program untuk prosedur menyeberang()")
    pindah = str(input("Tuliskan yang ingin di pindahkan ke seberang = "))
    pindah = pindah.upper()
    if (pindah == 'S'):
        if ('S' in list_kiri and 'P' in list_kiri):
            list_kiri.remove('S')
            list_kiri.remove('P')
            list_kanan.append('S')
            list_kanan.append('P')
        elif('S' in list_kanan and 'P' in list_kanan):
            list_kanan.remove('S')
            list_kanan.remove('P')
            list_kiri.append('S')
            list_kiri.append('P')
        else:
            print("Object hanya bisa berpindah dengan petani !")
            input()
    elif (pindah == 'D'):
        if ('D' in list_kiri and 'P' in list_kiri):
            list_kiri.remove('D')
            list_kiri.remove('P')
            list_kanan.append('D')
            list_kanan.append('P')    
        elif ('D' in list_kanan and 'P' in list_kanan):
            list_kanan.remove('D')
            list_kanan.remove('P')
            list_kiri.append('D')
            list_kiri.append('P')            
        else:
            print("Object hanya bisa berpindah dengan petani !") 
            input()
    elif (pindah == 'J'):
        if ('J' in list_kiri and 'P' in list_kiri):
            list_kiri.remove('J')
            list_kiri.remove('P')
            list_kanan.append('J')
            list_kanan.append('P')     
        elif ('J' in list_kanan and 'P' in list_kanan):
            list_kanan.remove('J')
            list_kanan.remove('P')
            list_kiri.append('J')
            list_kiri.append('P')          
        else:
            print("Object hanya bisa berpindah dengan petani !")    
            input()
    elif (pindah == 'P'):
        if ('P' in list_kiri):
            list_kiri.remove('P')
            list_kanan.append('P')
        else:
            list_kanan.remove('P')
            list_kiri.append('P')
    elif (pindah ==""):
        pass
    else:
        print("Error ! Yang di pindahkan hanya bisa petani saja / petani + 1 object ( serigala, domba, atau jagung ) !")

def cek_selesai(list_kiri, list_kanan):#fungsi ada return karena mengembalikan sebuah nilai ke yang memanggil (ada prosedur / tidak ada prosedur ?)
    #print("silakan isi kode program untuk prosedur tampil_gambar()") Prosedur = tidak ada return karena tidak mengembalikan nilai, hanya mengembalikan prosedur ke yang memanggil
    if (len(list_kanan) == len(menang) ):
        print("Selamat Anda Berhasil memindahkan petani,jagung,domba,dan serigala ke seberang dengan aman !")
        print("Anda berhasil memenangkan game dalam : ",score," Langkah !")
        selesai = True
        return selesai
    elif(list_kiri == kalah_1) or (list_kanan == kalah_1) or (list_kiri == kalah_2) or (list_kanan == kalah_2):
        print("Game over ! Jagung / Domba anda telah dimakan oleh domba / serigala !")
        selesai = True
        return selesai
    else:
        selesai = False
        return selesai
#program utama
os.system("cls")
list_kiri = ['P','J','D','S']
list_kanan = []
kalah_1 = ['D','S']
kalah_2 = ['J','D']
menang = ['P','J','D','S']
perahu_di_kanan = "~~~~~~~~~~(_____)"
perahu_di_kiri = "(_____)~~~~~~~~~~"
score = 0
selesai = False     #False jika permainan belum berakhir. True jika permainan berakhir
main_lagi = 'Y'     #'Y' jika user ingin bermain lagi. 'T' jika user tidak ingin bermain lagi

tampil_gambar(list_kiri, list_kanan)

while (main_lagi.upper() == 'Y'):
    menyeberang(list_kiri, list_kanan)
    list_kiri = sorted(list_kiri)
    list_kanan = sorted(list_kanan)
    kalah_1 = sorted(kalah_1)
    kalah_2 = sorted(kalah_2)
    score = score + 1
    os.system("cls")

    tampil_gambar(list_kiri, list_kanan)

    selesai = cek_selesai(list_kiri, list_kanan)

    #jika selesai = True, tanya apakah mau main lagi atau tidak
    if (selesai == True):
        main_lagi = input("\nMain lagi (Y/T)? ")

        #jika main_lagi = 'Y', reset lagi list_kiri dan list_kanan
        if ( main_lagi == "y" or main_lagi == "Y"):
            selesai = False
            score = score - score
            os.system("cls")
            list_kiri = ['P', 'J', 'D', 'S']
            list_kanan = []
            tampil_gambar(list_kiri, list_kanan)
        
        