# -*- coding: utf-8 -*-
"""
@Materi: Control Structure II
@Judul: Praktikum 4 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""
"""
s = int(input("masukkan angka: "))
p = int(input("masukkan pangkat: "))

total = 1
n = 1
while n <= p:
    total = total * s
    n = n + 1
print(total)
"""
"""

for i in [1,2,3,4,5]:
    print (i)
    
for i in range(5):
    print(i)
    
for i in harga:
    print (i)
"""

"""
ulangi = 0

while (ulangi < 10):
  print("Kuulangi ", ulangi, " kali")
  ulangi = ulangi + 1
"""
"""
for i in range(5):
    print("Nilai i adalah ", i)
	
for i in range(3,10):
    print("Kuulangi sebanyak ", i, "kali")

for i in range(30,20,-2):
    print("Aku mundur dari 30 ", i)

"""
n = ''
c = 0
t = 0
while (n != 0):
    n = int(input("masukkan 0 jika sudah tidak ada data: "))
    c += n
    t += 1
avg = c/(t-1)
print("nilai rata-rata adalah: ", avg)
