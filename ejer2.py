import pandas as pd

# 1. Cargar el archivo
df = pd.read_csv('dataset_kimball_ventas.csv', encoding='latin-1')

# 2. Ver las primeras 5 lineas 
print("\n ----- Primeras 5 lineas -----")
print(df.head(5))

# 3. Ver las ultimas 10 lineas 
print("\n ----- Ultimas 10 lineas -----")
print(df.tail(10))

# 4. Ver la informacion general 
print("\n ------ Informacion general ------")
df.info() # .info() ya imprime por sí solo, no necesita print()

# 5. Crear columna 'total_venta'(cantidad * precio)
df['total_venta'] = df['cantidad'] * df['precio_unitario']

# 6. Seleccionar solo las columnas 'cliente', 'producto' y 'total_venta'
print("\n ------ Seleccion de columnas ------")
print(df[['cliente', 'producto', 'total_venta']])

# 7. Filtrar: Solo las ventas de la categoría 'Electronica' y 'Accesorios'
print("\n ------- Solo las ventas de la categoría 'Electronica' y 'Accesorios' --------")
categoria = df[(df['categoria'] == 'Electronica') | (df['categoria'] == 'Accesorios')]
print(categoria)

# 8. Filtrar: Solo las ventas de los productos 'Laptop', 'Mouse'
print("\n ------- Solo las ventas de los productos 'Laptop', 'Mouse' --------")
laptop_mouse = df[(df['producto'] == 'Laptop') | (df['producto'] == 'Mouse')]
print(laptop_mouse)

# 9. Filtrar: Solo las ventas del cliente 'Ana Torres'
print("\n ------- Ventas de Ana Torres --------")
ana = df[df['cliente'] == 'Ana Torres']
print(ana)

# 10. Filtrar: Solo las ventas de la ciudad 'CDMX' y 'Monterrey'
print("\n ------- Ventas en CDMX y Monterrey --------")
# OJO: Asegúrate de si la columna se llama 'ciudad_cliente' o solo 'ciudad'
ciudad = df[(df['ciudad_cliente'] == 'CDMX') | (df['ciudad_cliente'] == 'Monterrey')]
print(ciudad)

# 11. Mostrar el total de ventas por sucursal.
print("\n ------ Totales por sucursal ------")
print(df.groupby('sucursal')['total_venta'].sum())

# 12. Mostrar el total de ventas por cliente
print("\n ------ Totales por cliente ------")
print(df.groupby('cliente')['total_venta'].sum())

# 13. Mostrar el total de ventas por vendedor
print("\n ------ Totales por vendedor ------")
print(df.groupby('vendedor')['total_venta'].sum())

# 14. Mostrar el total de ventas por ciudad
print("\n ------ Totales por ciudad ------")
print(df.groupby('ciudad_cliente')['total_venta'].sum())

# 15. Mostrar la cantidad de productos vendidos por cada producto
print("\n ------ Cantidad vendida por cada producto ------")
print(df.groupby('producto')['cantidad'].sum())

# 16. Mostrar el precio unitario máximo
maximo = df['precio_unitario'].max()
print(f"\nEl precio unitario máximo es -> {maximo}")

# 17. Mostrar el precio unitario minimo 
minimo = df['precio_unitario'].min()
print(f"El precio unitario mínimo es -> {minimo}")

# 18. Mostrar el promedio de ventas ('cantidad')
promedio_cant = df['cantidad'].mean()
print(f"El promedio de cantidad vendida es -> {round(promedio_cant, 2)}")

# 19. Calcular el promedio del precio_unitario
promedio_precio = df['precio_unitario'].mean()
print(f"El precio promedio unitario es -> {round(promedio_precio, 2)}")
