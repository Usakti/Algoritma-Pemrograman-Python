# -*- coding: utf-8 -*-
"""
@Materi: Recursive Function
@Judul: Praktikum 8 Latihan 2
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

"""
def perpangkatan(angka,pangkat):
    if(pangkat == 1):
        return(angka)
    else:
        return (angka * perpangkatan(angka,pangkat-1))

angka=int(input("Masukkan Angka: "))
pangkat=int(input("Masukkan Pangkat: "))
print("Hasil: ",perpangkatan(angka,pangkat))
"""

"""
x = 0
y = 0

def pangkat (x, y):
    if x != 0 or y != 0:
        return str (x**y)
    else:
        if x == 0:
            return "Error"
        if y == 0:
            return 1

x = int(input("masukkan bilangan awal: "))
y = int(input("masukkan bilangan pangkatnya: "))

hasil = pangkat (x, y)

print("hasil pangkat dari", x, "dengan pangkat", y, "adalah", hasil)
"""

def power(a,b):
    if a == 0 and b == 0:
        return " ERROR "
    elif b == 0:
        return 1
    elif b < 0:
        y = -(b)
        x = power(a,y)
        return 1/x
    else:
        return a * power(a,b-1)
    

while True:
    print("\nIni merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    x = (input("Masukkan Angka: "))
    if x == "":
        print("Program Selesai")
        break
    else:
        y = (input("Masukkan Pangkatnya: "))
        x,y = int(x), int(y)
        print("Hasilnya adalah: " + str(power(x,y)))
