import pandas as pd
from math import log 
import numpy as np

s = pd.Series(['Programacion Web', 'Computo en la nube', 'Base de datos', 'Ingeneria del conocimiento'])
sn = pd.Series([10,35,76,23,12])

print(s)
print(sn)


s = pd.Series({'Programacion Web':86,'Computo en la nube':90,'Base de datos':79,'Ingeneria del conocimiento':80})
print(s)

#Atributos de una serie, size, index, type
s = pd.Series([10,35,76,23,12])
print("Atributos de una serie")
print(s.size)
print(s.index)
print(s.dtype)

#Acceder a los elementos de una serie 
i = 1 
print("Acceso por posicion, elemento 2 -> {s[i]}")

s = pd.Series({'Programacion Web':86,'Computo en la nube':90,'Base de datos':79,'Ingeneria del conocimiento':80})
print("\nAcceso por indice, calif de la materia computo en la nube -> {s['Computo en la nube']}")
print("\nAcceso por indice, calif de la materia computo en la nube y Base de datos ->")
print(s[['Computo en la nube', 'Base de datos']])

s = pd.Series([10,35,76,23,12])

#Funciones para series 
print(f"Count {s.count()}")
print(f"Sum {s.sum()}")
print(f"Min {s.min()}")
print(f"Max {s.max()}")
print(f"Mean {s.mean()}")

#Aplicar operaciones a una serie 
s = pd.Series([1,2,3,4])
print(s*2)
print(s+10)
print(s / 2)

s = pd.Series(["a","b", "c"])
print(s*4)

#Aplicar funciones a una serie 
s = pd.Series([1,2,3,4])
print(s.apply(log))

s = pd.Series(["a","b","c"])
print(s.apply(str.upper))

#Filtar una serie 
s = pd.Series({'Programacion Web':86,'Computo en la nube':90,'Base de datos':79,'Ingeneria del conocimiento':79})
print(s[s>=80])

#Ordenar una serie 
print(s.sort_values())
print(s.sort_values(ascending=False))

#Eliminar datos desconocidos None NaN
s = pd.Series([1,2,None,3,4,np.nan, 5])
print(s.dropna())
