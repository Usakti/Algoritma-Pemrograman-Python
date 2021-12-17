# -*- coding: utf-8 -*-
"""
@Materi: Pengantar Data Science
@Judul: Praktikum 12 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

import pandas as pd

data = {"Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia"],
        "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brazilia", "Moskow"],
        "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia"],
        "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098],
        "Populasi": [264, 143, 1252, 1357, 329, 210, 146] }

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(df)
print(mean)
print(std)