# -*- coding: utf-8 -*-
"""
@Materi: Search, List & Sorting
@Judul: Praktikum 10 Latihan 2
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

def tukar(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubbleSort(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            tukar(A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)

A = [3, 5, 8, 4, 1, 9, -2]
bubbleSort(A, len(A))
print("List yang sudah disorting")
print(A)

