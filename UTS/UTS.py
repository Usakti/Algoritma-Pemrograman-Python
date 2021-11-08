# -*- coding: utf-8 -*-
"""
@Materi: UTS
@Judul: Praktikum Pembahasan UTS
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

print("----- No 3 -----")

x=2 
y=9 
z=2 
r=False

a = (r or (y>x)) and (2>=x) 
b = (x+y)>=(13-z) 
c = (y==9) and ((x>2) or r) 
d = (x !=z) or (not(r and y<10))

print("Jawaban a: " + str(a))
print("Jawaban b: " + str(b))
print("Jawaban c: " + str(c))
print("Jawaban d: " + str(d))

print("\n----- No 4 -----")
D=int(input("Input Nilai: ")) 
if D%2 != 0: 
    if D>1: 
        print("SALAM 1") 
    else: 
        print("SALAM 2") 
else:
    if D>=2:
        print("SALAM 3") 
    else: 
        print("SALAM 4") 


print("\n----- No 5 -----")

N = 1024 
L= 0 
E=1 
while E < N: 
    L += 1 
    E = E*2
    
print("L: " + str(L) + ", E: " + str(E))

print("\n----- No 8 -----")
buah = ['mangga', 'pisang', 'jambu', 'salak', 'rambutan', 'kecapi'] 
for i in range(len(buah)): 
    j = i // 2 
    if j > 1: 
        print(buah[i])

print("\n----- No 9 -----")
i = 0
for b in range(3, 11): 
    for i in range(b+1): 
        print("*", end="") 
    print() 

print("\nJawaban No 9")
b=3
while b<11:
    i=0
    while i<=b:
        print("*",end="")
        i+=1
    print()
    b+=1

print("\n----- No 10 -----")
x = input("Masukkan Nama: ")
y = input("Masukkan NIM: ")
z = '20'+y[-7]+y[-6]

x = x.split()
x = x[-1]

y = y[-2:]

print("UserID Anda: " + x + y + z)

print("\n----- No 11 -----")

import math

a = int(input("Masukkan Angka A: "))
b = int(input("Masukkan Angka B: "))

if(b < a):
    print("Nilai A harus lebih kecil dari B")
else:
    while(a<=b):
        kuadrat = math.sqrt(a)
        if((kuadrat%2 == 0) or (kuadrat%2 == 1)):
            kuadrat*=kuadrat
            print(int(kuadrat))
            a+=1
        else:
            a+=1

print("\n----- No 12 -----")

batas = 20
i = 1

nilaiPertama = 2*i + 1

while(i<=batas):
    nilai = 2*i + 1
    i+=1
#    nilai+=nilai
    
nilaiTerakhir = nilai #/2

hasil = batas*((nilaiPertama+nilaiTerakhir)/2)
    
print("Hasilnya adalah: " + str(hasil))
