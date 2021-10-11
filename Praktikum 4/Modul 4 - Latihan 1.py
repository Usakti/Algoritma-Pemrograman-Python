# -*- coding: utf-8 -*-
"""
@Materi: Control Structure II
@Judul: Praktikum 4 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

# Versi 1
a = int(input("masukkan jumlah maksimal: "))
for i in range(a, 0, -1):
    print(i)
    for j in range(0, i):
        print(i, end='')
    print()

# Versi 2
a = int(input("masukkan jumlah maksimal: "))
for i in range(-1, a):
    for j in range(-1, a - 1):
        print(a , end='')
    a -= 1
    print('')
