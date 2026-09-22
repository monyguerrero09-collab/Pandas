import pandas as pd 

# 1. Cargar el archivo 
df = pd.read_csv('dataset_kimball_ventas_2.csv', encoding='latin-1')

# 2. Ver las primeras 5 líneas 
print("\n1. --- Primeras 5 líneas ---")
print(df.head(5))

# 3. Ver las últimas 10 líneas 
print("\n2. --- Últimas 10 líneas ---")
print(df.tail(10))

# 4. Mostrar la información 
print("\n3. --- Información técnica ---")
df.info()

# 5. CONVERSIÓN DE FECHA 
df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True)
print("\n4. --- Fecha convertida correctamente ---")

# 6. Crear la columna 'total_venta' (cantidad * precio_unitario)
df['total_venta'] = df['cantidad'] * df['precio_unitario']
print("5. --- Columna 'total_venta' generada ---")

# 7. Seleccionar y mostrar solo las columnas: cliente, producto y total_venta
print("\n6. --- Selección de columnas específicas ---")
print(df[['cliente', 'producto', 'total_venta']].head())

# 8. Filtrar ventas donde la cantidad es mayor a 10
print("\n7. --- Ventas con cantidad > 10 ---")
print(df[df['cantidad'] > 10])

# 9. Filtrar registros del producto específico 'Producto_57'
print("\n8. --- Búsqueda de Producto_57 ---")
print(df[df['producto'] == 'Producto_57'])

# 10. Filtrar registros del cliente específico 'Cliente_460'
print("\n9. --- Búsqueda de Cliente_460 ---")
print(df[df['cliente'] == 'Cliente_460'])

# 11. Filtrar registros de la tienda específica 'Tienda_48'
print("\n10. --- Búsqueda de Tienda_48 ---")
print(df[df['tienda'] == 'Tienda_48'])

# 12. Calcular el total de ventas (monto) por cada tienda
print("\n11. --- Total de ventas por tienda ---")
print(df.groupby('tienda')['total_venta'].sum())

# 13. Calcular el total de ventas (monto) acumulado por cada cliente
print("\n12. --- Total de ventas por cliente ---")
print(df.groupby('cliente')['total_venta'].sum())

# 14. Obtener la cantidad total de unidades vendidas por producto
print("\n13. --- Cantidad total por producto ---")
print(df.groupby('producto')['cantidad'].sum())

# 15. Mostrar estadísticas generales: Precios extremos y Promedios
print("\n14. --- Estadísticas de precios ---")
print(f"Máximo: ${df['precio_unitario'].max()} | Mínimo: ${df['precio_unitario'].min()}")
print(f"Precio Promedio: ${round(df['precio_unitario'].mean(), 2)}")

print("\n15. --- Estadísticas de cantidades ---")
print(f"Promedio de cantidad vendida: {round(df['cantidad'].mean(), 2)} unidades")
