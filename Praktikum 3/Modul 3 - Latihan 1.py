# -*- coding: utf-8 -*-
"""
@Materi: Control Structure
@Judul: Praktikum 3 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

print ("program ini untuk mengetahui jenis dari suatu segitiga dengan berdasarkan panjang sisi yang diberikan")

import math

a = int(input("Panjang sisi A = "))
b = int(input("Panjang sisi B = "))
c = int(input("Panjang sisi C = "))

if (a == b == c):
    print("ini merupakan segitiga sama sisi")
elif (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("ini bukan merupakan segitiga")
elif ((a == b) or (b == c) or (c == a)):
    print("ini merupakan segitiga sama kaki")
elif ((a == math.sqrt(b**2 + c**2)) or (c == math.sqrt(b**2 + a**2)) or (b == math.sqrt(a**2 + c**2))):
    print("ini merupakan segitiga siku siku")
else:
    print("ini merupakan segitiga sembarang")
