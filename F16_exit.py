from F14_save import save
from load_data import *
# (F16) Mendefinisikan Fungsi Exit
def exit(username_arr,password_arr,role_arr,data_candi,data_bahan_bangunan) :
    inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while (inp != "y" and inp != "n" and inp != "Y" and inp != "N"):
        print("\nInput salah!")
        inp = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if inp == "Y" or inp == "y" :
        save(username_arr,password_arr,role_arr,data_candi,data_bahan_bangunan)