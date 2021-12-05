# -*- coding: utf-8 -*-
"""
@Materi: Search, List & Sorting
@Judul: Praktikum 10 Latihan 1
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

def binarySearch(arr, start, end, x):
    if end >= start:
        mid = start + (end- start)//2
        if arr[mid] == x: 
            return mid
        elif arr[mid] > x: 
            return binarySearch(arr, start, mid-1, x)
        else: 
            return binarySearch(arr, mid+1, end, x)
    else:
        return -1

def bubbleSort(x):
    for j in range(len(x)):
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]

    c = int(input("Masukkan angka yang dicari: "))
    print("Sesudah di Sorting: ", x)
    return binarySearch(x, 0, len(x)-1, c)


array = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
result = bubbleSort(array)

if result != -1: 
    print ("Elemen ditemukan pada posisi ke-" + str(result+1))
else: 
    print ("Elemen tidak ditemukan pada list")


"""
def binarySearchAppr (arr, start, end, x):
    if end >= start:
        mid = start + (end- start)//2
        if arr[mid] == x: 
            return mid
        elif arr[mid] > x: 
            return binarySearchAppr(arr, start, mid-1, x)
        else: 
            return binarySearchAppr(arr, mid+1, end, x)
    else:
        return -1

array = [1,3,24,18,17,42,35,29]
print("Sebelum di Sorting", array)
arr = sorted(array)
print("Sesudah di Sorting", arr)
x = 42

result = binarySearchAppr(arr, 0, len(arr)-1, x) 

if result != -1: 
    print ("Element ditemukan pada posisi ke-"+str(result+1))
else: 
    print ("Element tidak ditemukan pada list")
"""