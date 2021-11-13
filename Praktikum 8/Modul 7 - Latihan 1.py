# -*- coding: utf-8 -*-
"""
@Materi: Function Exercise
@Judul: Praktikum 7 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

#Versi 1
def Prima(x):
    if x <= 1:
        return False
    for i in range (2, x):
        if x % i == 0:
            return False
    return True

def Main():
    angka = int(input("Masukkan angka: "))
    if Prima(angka):
        print (angka, "adalah bilangan Prima")
    else:
        print (angka, "bukanlah bilangan Prima")
        
Main()

#Versi 2
def prima(angka):
    for i in range(2, angka):
        if (angka % i) ==  0:
            return print (angka, "bukan bilangan prima\n", i, "kali", angka//i, "=", angka)
        else:
            return print (angka, "adalah bilangan prima")

def notprima(angka):
    if angka > 1:
        prima(angka)
    else:
        print (angka, "bukan bilangan prima")

angka = int(input("masukkan bilangan: "))
notprima(angka)
