# main.py
# Menjadi file utama untuk menjalankan program

# import
from commands import run
from load_data import *


# ALGORITMA UTAMA
# Mendeklarasikan variabel role yang menentukan fungsi yang dapat diakses
# Melakukan looping untuk terus meminta prompt

if username_arr != None and password_arr != None and role_arr != None and data_candi != None and data_bahan_bangunan != None : 
    while True:
        prompt = input(">>> ")  
        run(prompt)
        if prompt == "exit":
            break
    