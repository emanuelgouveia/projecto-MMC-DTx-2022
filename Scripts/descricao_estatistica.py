# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 23:06:56 2022

@author: duart
"""

import pandas as pd

N = 14567
n = 196

dist = [81, 60, 79, 72, 74, 77, 68, 81, 76, 59, 73, 64, 76, 79, 78, 81, 68, 82, 75, 80, 73, 78, 71, 81, 72, 60, 66, 76, 80, 76, 78, 71, 74, 78, 74, 71, 67, 73, 63, 69, 63, 66, 83, 76, 59, 84, 63, 77, 67, 75, 80, 73, 78, 73, 72, 89, 64, 79, 76, 67, 74, 65, 75, 56, 83, 76, 66, 64, 70, 78, 65, 83, 75, 76, 71, 74, 72, 71, 90, 76, 79, 81, 71, 79, 77, 83, 81, 71, 78, 77, 69, 68, 67, 71, 79, 72, 73, 79, 51, 61, 75, 68, 73, 79, 83, 76, 80, 81, 77, 82, 73, 86, 74, 80, 84, 68, 77, 70, 60, 78, 80, 133, 84, 73, 79, 74, 76, 70, 67, 73, 73, 78, 77, 63, 77, 46, 80, 73, 80, 75, 63, 59, 71, 84, 78, 78, 77, 82, 79, 64, 79, 66, 82, 79, 78, 73, 69, 55, 65, 81, 85, 71, 65, 81, 83, 76, 89, 73, 69, 78, 82, 82, 81, 76, 51, 71, 79, 71, 83, 75, 65, 83, 71, 76, 68, 68, 74, 81, 75, 81, 80, 77, 77, 80, 79]
dist.sort()

df = pd.DataFrame(dist, columns = ["Nº de ocorrências por classe"])
df.plot.hist()
def describe(df, stats):
    d = df.describe()
    return d.append(df.reindex(d.columns, axis = 1).agg(stats))

ds = describe(df, ['skew', 'kurt']) #skew > 0, inclinação para a direita, i.e., maior densidade à direta
#curtose relativamente elevada indicia caudas pesadas

cv = round(float(df.std()/df.mean()),5) # 0.11406, por isso há pouca variação nos tamanhos

             
ds.append(df.mode()) #as modas



 
