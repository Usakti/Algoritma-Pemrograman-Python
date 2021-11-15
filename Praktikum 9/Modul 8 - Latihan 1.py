# -*- coding: utf-8 -*-
"""
@Materi: Recursive Function
@Judul: Praktikum 8 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

"""
def fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return (fibo(a-1)+fibo(a-2))
a = int(input("masukkan angka: "))
if a < 1:
    print("angka harus diatas 0")
print (fibo(a))
"""

"""
def fib(n):
    if (n <= 2):
        return 1
    else:
        return (fib(n-1)+fib(n-2))
print ("fungsi untuk menampilkan deret fibonacci sebanyak x buah")
n = int (input("masukkan x:"))
for i in range (1,n):
    print (fib(i))
"""

def fibonacci(x):
  if x<=2:
    return 1
  else:
    fib = fibonacci(x-1)+fibonacci(x-2)
  return fib

print('Menghitung bilangan fibonacci menggunakan fungsi rekursif')
angka = int(input('Masukkan sebuah bilangan '))
fibonacci_bil = fibonacci(angka)
print('Bilangan fibonacci ke-'+str(angka)+' adalah '+str(fibonacci_bil))