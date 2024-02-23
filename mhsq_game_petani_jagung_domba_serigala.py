#================================================================================
#Program Petani-Domba-Jagung-Serigala
#Pemain harus memindahkan petani, domba, jagung, dan serigala ke seberang sungai 
#menggunakan perahu yang hanya dapat memuat petani dan satu bawaan
#================================================================================
#import library
import os

#sub program (prosedur dan fungsi)
def tampil_gambar(list_kiri, list_kanan):
    print("Pindahkan Petani (P), Jagung (J), Domba (D), dan Serigala (S) ke sisi kanan!")
    print()
    if ('P' in list_kiri):
        print(list_kiri,"\t\t\t\t",list_kanan)
        print("=============== \____/,,,,,,,,,, ===============")

    else:
        print(list_kiri,"\t\t\t\t",list_kanan)
        print("=============== ,,,,,,,,,,,\____/ ===============")


    #print("silakan isi kode program untuk prosedur tampil_gambar()")
    
def menyeberang(list_kiri, list_kanan):
    pilih=input("Seberangkan (J, D, S): ")
    if ("P" in list_kiri):
        if (pilih.upper()=="p"):
            list_kanan.append("P") 
            list_kiri.remove("P")

        else:
            (pilih.upper()==pilih in list_kiri and 'P' in list_kiri)
            list_kanan.append(pilih)
            list_kanan.append("P")
            list_kiri.remove("P")
            list_kiri.remove(pilih)

    elif ("P" in list_kanan):
        if (pilih.upper()=="p"):
            list_kiri.append("P") 
            list_kanan.remove("P")

        elif (pilih.upper()==pilih in list_kanan and 'P' in list_kanan):
            list_kanan.remove('P')
            list_kanan.remove(pilih)
            list_kiri.append('P')
            list_kiri.append(pilih)

        else:
            print("Pilihan Anda Berseberangan Dengan 'P' ! ")
            input("Enter")


    #print("silakan isi kode program untuk prosedur menyeberang()")

def cek_selesai(list_kiri, list_kanan):
    if (list_kiri==['J', 'D', 'S']):
        print("Oooppss, Anda gagal. Jagungnya habis dimakan Domba!")
    elif (list_kiri==['D', 'S']):
        print("Oooppss, Anda gagal. Dombanya mati dimakan Serigala!")
    elif (list_kiri==['J', 'D']):
        print("Oooppss, Anda gagal. Jagungnya habis dimakan Domba!")
    #print("silakan isi kode program untuk prosedur tampil_gambar()")

#program utama
os.system("cls")
list_kiri = ['P', 'J', 'D', 'S']
list_kanan = []
selesai = False     #False jika permainan belum berakhir. True jika permainan berakhir
main_lagi = 'Y'     #'Y' jika user ingin bermain lagi. 'T' jika user tidak ingin bermain lagi

tampil_gambar(list_kiri, list_kanan)

while (main_lagi.upper() == 'Y'):
    menyeberang(list_kiri, list_kanan)

    os.system("cls")
    tampil_gambar(list_kiri, list_kanan)

    selesai = cek_selesai(list_kiri, list_kanan)

    # jika selesai = True, tanya apakah mau main lagi atau tidak
    if (selesai):
        main_lagi = input("\nMain lagi (Y/T)? ")

        #jika main_lagi = 'Y', reset lagi list_kiri dan list_kanan
        os.system("cls")
        list_kiri = ['P', 'J', 'D', 'S']
        list_kanan = []
        tampil_gambar(list_kiri, list_kanan)