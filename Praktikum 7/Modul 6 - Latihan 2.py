# -*- coding: utf-8 -*-
"""
@Materi: Function
@Judul: Praktikum 6 Latihan 2
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

print ("Program ini akan menentukan jumlah hari dalam bulan tertentu")

F = False

year = ''

def Kabisat(year):
    year = int(input("masukkan tahun (e.g., 2019): "))
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        print("29 hari dalam sebulan")
    else:
        print("28 hari dalam sebulan")
    
def NonKabisat(bulan):
    if bulan in [0, 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12]:
        if bulan in [4, 6, 9, 11]:
            print("30 hari dalam sebulan")
        elif bulan in [1, 3, 5, 7, 8, 10, 12]:
            print("31 hari dalam sebulan")
        elif bulan == 2:
            Kabisat(year)
    else:
        print("Error")
            
while (not F):
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("masukkan bulan (1-12): "))
    if bulan == 0:
        F = True
    else:
        NonKabisat (bulan)
    
print ("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")