# -*- coding: utf-8 -*-
"""
@Materi: Operasi Aritmatika
@Judul: Praktikum 2 Latihan 2
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

import math

t1 = float(input("masukkan lattitude kota pertama = "))
g1 = float(input("masukkan longitude kota pertama = "))

t2 = float(input("masukkan lattitude kota kedua = "))
g2 = float(input("masukkan longitude kota kedua = "))

dlat = t2 - t1
dlon = g2 - g1

a = math.sin(math.radians(dlat/2)) ** 2 + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) ** 2

# Versi Arc sinus
c = 2 * math.asin(math.sqrt(a))

# Versi Arc tangen 2
#c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
r = 6371.01

print("jarak antara dua titik adalah" , c*r , "kilometer")