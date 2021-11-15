# -*- coding: utf-8 -*-
"""
@Materi: Recursive Function
@Judul: Praktikum 8 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

def rekursif(angka):
    if angka > 0:
        print (angka)
        angka = angka - 1
        rekursif(angka)
    else:
        print(angka)
        
masukkan = int(input("masukkan angka: "))
rekursif(masukkan)

def mystery(x):
    if x == 0:
        return 0
    else:
        return (x%10) + mystery(x//10)
    
bil = int(input("masukkan nilai: "))
print("Mysteryous: " + str(mystery(bil)))



def kalikan (a, b):
    if b == 1:
        return a
    else:
        return (a + kalikan(a, b-1))

print(kalikan (10, 5))



def faktorial (x):
    if x == 1:
        return 1
    else:
        return (x * faktorial(x-1))

# Cara Kerja Fungsi Rekursif
# 4 * faktorial(4 - 1) == 24 ---> Nilai Akhir
# 3 * faktorial(3 - 1) == 6
# 2 * faktorial(2 - 1) == 2
# 1
    
bil = int(input("Masukkan angka: "))
print ("Faktorial dari", bil, "adalah", faktorial (bil))
