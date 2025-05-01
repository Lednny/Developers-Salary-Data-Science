import pandas as pd
import os 

media = datos.mean()
mediana = datos.median()
moda = datos.mode()[0]  

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda.tolist()) 
