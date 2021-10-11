# -*- coding: utf-8 -*-
"""
@Materi: Control Structure II
@Judul: Praktikum 4 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

a = int(input("masukkan jumlah maksimal: "))
for i in range(-1, a):
    for j in range(-1, a - 1):
        print(a , end='')
    a -= 1
    print('')