# -*- coding: utf-8 -*-
"""
@Materi: Recursive Function
@Judul: Praktikum 8 Bonus
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

def int2hex(n):
    x=n%16
    if n > 15:
        int2hex(int(n/16))
    if x == 10:
        print ("A", end='')
    if x == 11:
        print ("B", end='')
    if x == 12:
        print ("C", end='')
    if x == 13:
        print ("D", end='')
    if x == 14:
        print ("E", end='')
    if x == 15:
        print ("F", end='')
    if x < 10:
        print (x, end='')
    return

def Hex2Dec (string):
    value = 0
    x = len(string)
    for i in range(x):
        b = string[i]
        if b == "A" or b == "a":
            b = 10
        elif b == "B" or b == "b":
            b = 11
        elif b == "C" or b == "c":
            b = 12
        elif b == "D" or b == "d":
            b = 13
        elif b == "E" or b =="e":
            b = 14
        elif b == "F" or b =="f":
            b = 15
        else:
            b = int(string[i])
        z = ((16**(x-(i+1)))*b)
        value += z
    return value

x = int(input("Tekan 1 untuk mengubah Desimal menjadi Hexadesimal\nTekan 2 untuk mengubah Hexadesimal menjadi Desimal\n"))
if x == 1:
    print("Program ini akan mengubah Desimal menjadi Hexadesimal, tekan -1 untuk mengakhiri")
    while True:
        x = int(input("\nmasukkan interger desimal "))
        if x == -1:
            break
        else:
            int2hex(x)
if x == 2:
    print("Program ini akan mengubah Hexadesimal menjadi Desimal, tekan -1 untuk mengakhiri")
    while True:
        x = str(input("\nmasukkan interger hexadesimal "))
        if x == "-1":
            break
        else:
            print(Hex2Dec(x))
            
print("program selesai")
