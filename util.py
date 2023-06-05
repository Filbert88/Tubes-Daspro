# util.py
# File ini digunakan untuk menyimpan semua fungsi/prosedur yang akan digunakan berulang kali dan atau
#   mendeklarasi dan mendefenisikan fungsi yang kita buat sendiri
import time
# Membuat fungsi setara .split() sendiri
def splitLuSendiri(sebaris:str, x:int)->int:
    # x adalah jumlah kolom di csv
    temp = ""
    hasil = ["%" for i in range (x)]
    j=0
    for i in range(len(sebaris)): #karena len string diperbolehkan
        if sebaris[i]==';' or i==len(sebaris)-1:
            if i == len(sebaris)-1 and sebaris[i]!="\n":
                temp += sebaris[i]
            hasil[j] = temp
            j+=1
            temp = ""
        else: temp += sebaris[i]
    return hasil

# Membuat fungsi setara len() untuk menghitung jumlah indeks yang berisi dari sebuah array yang panjangnya diketahui
def lenSendiri(data : list, N : int)-> int : 
    # N adalah panjang dari array
    panjang = 0
    for i in range(N):
        if data[i]!="%":
            panjang += 1
    return panjang

# untuk mengisi data di bahan bangunan
def isibahanbangunan(array : list) -> list:
    array[1] =['Pasir','pasir asli sunagakure','0']
    array[2] =['Batu','batu biasa bukan batu akik','0']
    array[3] =['Air','air mata TPB','0']
    return array

def kurangBerapa(tersedia : int, butuh : int) -> int:
    if tersedia >= butuh:
        return 0
    else:
        return butuh - tersedia
    
