# -*- coding: utf-8 -*-
"""
@Materi: Search, List & Sorting
@Judul: Praktikum 10 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

a = [60, 60, 47, 90, 80, 50, 63]
iniList = ["ini 1", "ini 2", "ini angka dst"]

print(iniList)

"""
# Iterative Binary Search Function
def binarySearch(arr, l, r, x): 

	while l <= r: 

		mid = (r+l)//2;
		if arr[mid] == x: 
			return mid
		elif arr[mid] < x: 
			l = mid + 1
		else: 
			r = mid - 1
	return -1


arr = [ 0, 13,22, 38, 44, 50, 66, 71, 89, 90, 103, 111 ] 
x = 0

result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
	print ("Element ditemukan pada index %d" % result) 
else: 
	print ("Element tidak ditemukan pada list")
"""

"""
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)
"""

"""
def bubbleSort(a):
	n = len(a)
	for i in range(n):
		for j in range(0, n-i-1):
			if a[j] > a[j+1] :
				a[j], a[j+1] = a[j+1], a[j]

a = [60, 60, 47, 90, 80, 50, 63]

bubbleSort(a)

print ("Urutannya adalah: ")
for i in range(len(a)):
	print ("%d" %a[i]), 
"""

"""
#Hard
def binary_search(l, num_find):
    start = 0
    end = len(l) - 1
    mid = (start + end)//2
    found = False
    position = -1

    while start <= end:
        if l[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > l[mid]:
            start = mid + 1
            mid = (start + end)//2
        else:
            end = mid - 1
            mid = (start + end)//2
            
    print("Sesudah di Sorting: ", l)
    return (found, position-1)

l = [77, 88, 82, 34, 47, 37, 68, 71, 89, 98]
num = 89
found = binary_search(l, num)
if found[0]:
    print('Nomor %d ditemukan di posisi %d'%(num, found[1]+2))
else:
    print('Nomor %d tidak ditemukan'%num)
"""
