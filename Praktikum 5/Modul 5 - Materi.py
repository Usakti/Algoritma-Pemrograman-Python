# -*- coding: utf-8 -*-
"""
@Materi: List & Dictionary
@Judul: Praktikum 5 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

# Tipe Data List
makanan = ['Nasi goreng', 'Bakso', 'Siomay']
minuman = ['Teh manis', 'Sprite', 'Thai tea']
harga = [1000, 2500, 1750, 4000]

# Tipe Data Dictionary
biodata = {'nama': 'Adi','id':2}

biodata['nama'] = 'Azhar' # Mengubah entri yang sudah ada
biodata['college'] = "Universitas Trisakti" # Menambah entri baru

# del biodata['name'] # hapus entri dengan key 'Name'
# biodata.clear()     # hapus semua entri di dict
# del biodata         # hapus dictionary yang sudah ada

print(biodata['college'])
print(biodata['nama'])
