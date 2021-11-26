# -*- coding: utf-8 -*-
"""
@Materi: File Handling & File Processing
@Judul: Praktikum 9 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

# Write File
file = open("Test.txt", "w")
file.write("Nadiya Amanda Rizkania")
file.close()

# Read File
file = open("Test.txt", "r")
text = file.read()
print(text)
file.close()

# Add Text
file = open("Test.txt", "a")
file.write(" - 20 Tahun - Jakarta")
file.close()

# Read & Write File
file = open("Test.txt", "r+")
text = file.read()
print(text)
file.close()
