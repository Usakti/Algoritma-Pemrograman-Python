# -*- coding: utf-8 -*-
"""
@Materi: Search, List, Sorting
@Judul: Praktikum 10 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

print("===== No 4 =====")

x = 'abcd'
for i in range(len(x)): 
    print(x[i]) 

x = 'abcd'
for i in range(len(x)):
    print(i)

x = 'abcd' 
for i in range(x): 
    print(i) 

x = 'abcd'
for i in range(x): 
    print(x[i])


print("===== No 5 =====")

#apple = mango

print("===== No 6 =====")

def C2F(c): 
	return c * 9/5 + 32

print(C2F(100)," ",C2F(0))

print("===== No 7 =====")

def example(a): 
	a = a + '2' 
	a = a * 2 
	return a 

print(example('hello'))

print("===== No 8 =====")

print('''andi 
\nbadu
\ncory''') 
'''
print('andi
\nbadu
\ncory')
''' 
print('andibaducory')
print('andi\nbadu\ncory')

print("===== No 9 =====")

list1 = [4, 2, 2, 4, 5, 2, 1, 0]

print(list1[0]) 
print(list1[:2]) 
print(list1[:-2]) 

print("===== No 10 =====")

list1 = [4, 2, 2, 4, 5, 2, 1, 0]

print(list1[:5]) 
print(list1[2:4]) 
print(list1[2:]) 
print(list1[2:5])


print("===== No 1 Essay =====")

#versi 1
nama = 'Azhar Zulma' #isi dengan nama anda (memuat 2 suku kata) 
vokal_nama = [] 

# Ambil semua huruf vokal dari variable nama,
# dan masukkan ke dalam list vokal_nama 
for i in range(len(nama)):
    if((nama[i] == 'A') or 
       (nama[i] == 'a') or 
       (nama[i] == 'I') or 
       (nama[i] == 'i') or 
       (nama[i] == 'U') or 
       (nama[i] == 'u') or 
       (nama[i] == 'E') or 
       (nama[i] == 'e') or 
       (nama[i] == 'O') or 
       (nama[i] == 'o')):
        vokal_nama += nama[i]
        #vokal_nama.append(nama[i])
        
print(vokal_nama)

#versi 2
vokal_nama = []

for karakter in nama:
  if karakter in ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']:
    vokal_nama += karakter
    
print(vokal_nama)

print("===== No 2 Essay =====")

def doSomething(a, b, c):
    if a==b: 
        if b==c: 
            return True 
        return False
    
print(doSomething(1,1,3))


print("===== No 3 Essay =====")

def min_gap(data):
    tampung = None
    lists = []
    for i in range(len(data)):
        if (i != 0):
            tampung = data[i] - data[i-1]
            lists.append(tampung)
    return bubbleSort(lists)

def bubbleSort(x):
    for j in range(len(x)):
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x[0]

data = [3, 5, 11, 4, 8]
        
print(min_gap(data))


print("===== No 4 Essay =====")

def looping(n):
    #Print higher to Lower
    for i in range(n - 1,0,-1):
        for j in range(i,-1,-1):
            print("*",end="")       
        print("")
    #Print Lower to Higher
    for i in range(n):
        for j in range(0,i+1):
            print("*",end="")       
        print("")

n = 4
looping(n)
