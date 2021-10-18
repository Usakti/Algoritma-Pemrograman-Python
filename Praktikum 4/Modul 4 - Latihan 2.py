# -*- coding: utf-8 -*-
"""
@Materi: Control Structure II
@Judul: Praktikum 4 Latihan 2
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

bosan = False

print ("This program will determine the number of days of a given month")
while (not bosan):
    print("Enter -1 to stop the program")
    month = int(input("Enter the month (1-12): "))
    
    if month in [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        if month == -1:
            bosan = True
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            print ("There are 31 days in the month")
        elif month in [4, 6, 9, 11]:
            print("There are 30 days in the month")
        elif month == 2:
            year = int(input("Please enter the year (e.g., 2021): "))
            if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
                print ("There are 29 days in the month")
            else:
                print("There are 28 days in the month")
    else:
        print("* Invalid value entered: ", month, " *")

print("Terima kasih sudah menggunakan program saya. Sampai berjumpa lagi.")