# -*- coding: utf-8 -*-
"""
@Materi: Control Structure
@Judul: Praktikum 3 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

b = float(input("Masukkan berat badan (dalam kilogram): "))
t = float(input("Masukkan tinggi badan (dalam meter): "))

bmi = b/(t*t)

if (bmi < 18.5):
    print("kamu termasuk Underweight")
elif (bmi >= 18.5) and (bmi >= 24.9):
    print("kamu termasuk Normal")
elif (bmi >= 25) and (bmi <= 29.9):
    print("kamu termasuk Overweight")
else:
    print("Kamu termasuk Obesitas")

"""
inputBulan = int(input("masukkan inputBulan: "))
inputTahun = int(input("masukkan tahun: "))

if(inputBulan >= 13 or inputBulan <= 0):
	print("Masukin bulan yg bener woi")
elif(inputBulan == 1 or inputBulan == 3 or inputBulan == 5 or inputBulan == 7 or inputBulan == 8 or inputBulan == 10 or inputBulan == 12):
	print("Ini 31 hari")
elif(inputBulan == 2):
    if(inputTahun % 4 == 0 and inputBulan == 2):
        print("Ini 29 hari")
    else: 
    	print("Ini 28 hari")
else:
	print("Ini 30 hari")
"""
