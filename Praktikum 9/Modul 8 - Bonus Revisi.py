# -*- coding: utf-8 -*-
"""
@Materi: Recursive Function
@Judul: Praktikum 8 Bonus
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

#mengkonversi char base16 menjadi base 10
def searchBase(char):
    if(char == "A"):
        return 10
    elif(char == "B"):
        return 11
    elif(char == "C"):
        return 12
    elif(char == "D"):
        return 13
    elif(char == "E"):
        return 14
    elif(char == "F"):
        return 15

#menyimpan result
cache = 0
#NUMBER ADALAH STRING YANG AKAN KITA CONVERT
#DEFAULT PARAMETER
def hexToBase10(number, pos = 0):
    #mereferensikan variabel global cache
   global cache
   # ""
   if (0 == len(number)):
       return cache
   # string "F" 
   num = number[len(number)-1] 
   #num = "F"
   
   #mengurangi character terakhir di number 
   number = number[:-1]
   #number = ""
   
   # jika sebuah string itu adalah angka interger
   # bakal return TRUE
   
   #check apakah num itu digit atau ga
   if(num.isdigit()):
       #convert string ke int
       num = int(num)
       # cache = cache + (2)
       # cache sekarang  = 2
       cache = cache + (num * (16 ** pos))
   else:
       cache = cache + (searchBase(num) * (16 ** pos))
    
    #number sudah di slice "F"
   return hexToBase10(number, pos+1)  


print(hexToBase10("FFF"))
