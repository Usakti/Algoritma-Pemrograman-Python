# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 08:21:52 2021

@author: Azhar Rizky Zulma
"""

import pandas as pd

df = pd.read_csv('Negara.csv', index_col=0)

mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Framenya:")
print(df, "\n")

print("Berikut Data Mean:")
print(mean, "\n")

print("Berikut Data Standard Deviation:")
print(std, "\n")