import pandas as pd

df = pd.read_csv('ventas.csv')

print("\n -----Primeras 5 lineas -----")
print(df.head(5))

print("\n ------ infromacion del DataFrame ------")
print(df.info())

#print("\n ------- Crear columna ------")
df ['total de venta'] = df['cantidad'] = df['precio unitario']
#print (df)

print("\n------ Totales por producto ------")
print(df(['producto', 'total_venta']))

print("\n ------- Productos electronica --------")
electronica = df[df['categoria'] == 'Electronica']
print(electronica)

print("\n -------- Precio promedio de los productos ----")
promedio = df['precio unitario'].mean()
print("EL precio promedio es -> {round(promedio.2)}")

promedio = df['precio unitario'].mean()
print("EL precio promedio es -> {round(promedio.2)}")