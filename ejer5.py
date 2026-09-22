import pandas as pd 

# 1. Cargar el archivo 
df = pd.read_csv('pokemon_analisis_final.csv', encoding='latin-1')

# 2. Ver las primeras 5 líneas 
print("\n1. --- Primeras 5 líneas ---")
print(df.head(5))

# 3. Ver las últimas 10 líneas 
print("\n2. --- Últimas 10 líneas ---")
print(df.tail(10))

# 4. Mostrar la información 
print("\n3. --- Información técnica ---")
df.info()