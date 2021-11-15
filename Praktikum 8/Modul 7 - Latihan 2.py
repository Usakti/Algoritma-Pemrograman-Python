# -*- coding: utf-8 -*-
"""
@Materi: Function Exercise
@Judul: Praktikum 8 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

print("Ordinal Number")
print("ketik 0 untuk mengentikan program")

def ordinalnumber(a):
    a == angka
    if a % 10 == 1:
        return a, "st"
    elif a % 10 == 2:
        return a, "nd"
    elif a % 10 == 3:
        return a, "rd"
    elif a % 10 in range (4, 21):
        return a, "th"
    elif a % 10 == 0:
        return a, "th"
    else:
        return ordinalnumber(a)

angka = ''

while angka != 0:
    angka = int(input("masukkan angka: "))
    print(ordinalnumber(angka))

print("terima kasih telah menggunakan program saya")
        