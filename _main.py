import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

tienda_1 = pd.read_csv('./data/tienda_1.csv')
tienda_2 = pd.read_csv('./data/tienda_2.csv')
tienda_3 = pd.read_csv('./data/tienda_3.csv')
tienda_4 = pd.read_csv('./data/tienda_4.csv')

tienda_sample = tienda_1.head()
print(tienda_sample)

ingreso_total_tienda_1 = tienda_1['Precio'].sum()
print(f'Ingreso total tienda 1: {ingreso_total_tienda_1}')

ingreso_total_tienda_2 = tienda_2['Precio'].sum()
print(f'Ingreso total tienda 2: {ingreso_total_tienda_2}')

ingreso_total_tienda_3 = tienda_3['Precio'].sum()
print(f'Ingreso total tienda 3: {ingreso_total_tienda_3}')

ingreso_total_tienda_4 = tienda_4['Precio'].sum()
print(f'Ingreso total tienda 4: {ingreso_total_tienda_4}')

categorias_tienda_1 = tienda_1.groupby('Categoría del Producto').count()
print(categorias_tienda_1['Producto'])

categorias_tienda_2 = tienda_2.groupby('Categoría del Producto').count()
print(categorias_tienda_2['Producto'])

categorias_tienda_3 = tienda_3.groupby('Categoría del Producto').count()
print(categorias_tienda_3['Producto'])

categorias_tienda_4 = tienda_4.groupby('Categoría del Producto').count()
print(categorias_tienda_4['Producto'])

calificacion_tienda_1= tienda_1['Calificación'].mean()
print(f'Calificación promedio tienda 1: {calificacion_tienda_1}')

calificacion_tienda_2 = tienda_2['Calificación'].mean()
print(f'Calificación promedio tienda 2: {calificacion_tienda_2}')

calificacion_tienda_3 = tienda_3['Calificación'].mean()
print(f'Calificación promedio tienda 3: {calificacion_tienda_3}')

calificacion_tienda_4 = tienda_4['Calificación'].mean()
print(f'Calificación promedio tienda 4: {calificacion_tienda_4}')

ventas_tienda_1 = tienda_1['Producto'].value_counts()
print(ventas_tienda_1)

producto_mas_vendido_tienda_1 = ventas_tienda_1.idxmax()
cantidad_mas_vendida_tienda_1 = ventas_tienda_1.max()
print(f'Producto más vendido tienda 1: {producto_mas_vendido_tienda_1}, con un total de {cantidad_mas_vendida_tienda_1} ventas.')

producto_menos_vendido_tienda_1 = ventas_tienda_1.idxmin()
cantidad_menos_vendida_tienda_1 = ventas_tienda_1.min()
print(f'Producto menos vendido tienda 1: {producto_menos_vendido_tienda_1}, con un total de {cantidad_menos_vendida_tienda_1} ventas.') # como hacer que me muestre los empates?

ventas_tienda_2 = tienda_2['Producto'].value_counts()
print(ventas_tienda_2)

producto_mas_vendido_tienda_2 = ventas_tienda_2.idxmax()
cantidad_mas_vendida_tienda_2 = ventas_tienda_2.max()
print(f'Producto más vendido tienda 2: {producto_mas_vendido_tienda_2}, con un total de {cantidad_mas_vendida_tienda_2} ventas.')

producto_menos_vendido_tienda_2 = ventas_tienda_2.idxmin()
cantidad_menos_vendida_tienda_2 = ventas_tienda_2.min()
print(f'Producto menos vendido tienda 2: {producto_menos_vendido_tienda_2}, con un total de {cantidad_menos_vendida_tienda_2} ventas.') 

ventas_tienda_3 = tienda_3['Producto'].value_counts()
print(ventas_tienda_3)

producto_mas_vendido_tienda_3 = ventas_tienda_3.idxmax()
cantidad_mas_vendida_tienda_3 = ventas_tienda_3.max()
print(f'Producto más vendido tienda 3: {producto_mas_vendido_tienda_3}, con un total de {cantidad_mas_vendida_tienda_3} ventas.')

producto_menos_vendido_tienda_3 = ventas_tienda_3.idxmin()
cantidad_menos_vendida_tienda_3 = ventas_tienda_3.min()
print(f'Producto menos vendido tienda 3: {producto_menos_vendido_tienda_3}, con un total de {cantidad_menos_vendida_tienda_3} ventas.') 

ventas_tienda_4 = tienda_4['Producto'].value_counts()
print(ventas_tienda_4)

producto_mas_vendido_tienda_4 = ventas_tienda_4.idxmax()
cantidad_mas_vendida_tienda_4 = ventas_tienda_4.max()
print(f'Producto más vendido tienda 4: {producto_mas_vendido_tienda_4}, con un total de {cantidad_mas_vendida_tienda_4} ventas.')

producto_menos_vendido_tienda_4 = ventas_tienda_4.idxmin()
cantidad_menos_vendida_tienda_4 = ventas_tienda_4.min()
print(f'Producto menos vendido tienda 4: {producto_menos_vendido_tienda_4}, con un total de {cantidad_menos_vendida_tienda_4} ventas.') 

promedio_envios_tienda_1= tienda_1['Costo de envío'].mean()
print(f'el promedio del costo de envios de la tienda 1 es: {promedio_envios_tienda_1}')

promedio_envios_tienda_2= tienda_2['Costo de envío'].mean()
print(f'el promedio del costo de envios de la tienda 2 es: {promedio_envios_tienda_2}')

promedio_envios_tienda_3= tienda_3['Costo de envío'].mean()
print(f'el promedio del costo de envios de la tienda 3 es: {promedio_envios_tienda_3}')

promedio_envios_tienda_4= tienda_4['Costo de envío'].mean()
print(f'el promedio del costo de envios de la tienda 4 es: {promedio_envios_tienda_4}')

#GRAFICO DE LINEAS DE INGRESO TOTAL POR TIENDA
ingreso_tiendas = {'X': ['tienda_1', 'tienda_2', 'tienda_3', 'tienda_4'], 'Y': [ingreso_total_tienda_1, ingreso_total_tienda_2, ingreso_total_tienda_3, ingreso_total_tienda_4]}
plt.plot(ingreso_tiendas['X'], ingreso_tiendas['Y'], marker='o', linestyle='-')
# Personalizar el gráfico
plt.xlabel('tienda')
plt.ylabel('total ventas')
plt.title('total de ingresos por cada tienda')
plt.grid()
plt.show() # Mostrar el gráfico


# GRAFICOS DE BARRAS DE CANTIDAD DE PRODUCTOS POR CATEGORIA
plt.figure(figsize=(10, 6))
categorias_tienda_1['Producto'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de productos por categoría tienda 1')
plt.xlabel('Categoría del Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
categorias_tienda_2['Producto'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de productos por categoría tienda 2')
plt.xlabel('Categoría del Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
categorias_tienda_3['Producto'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de productos por categoría tienda 3')
plt.xlabel('Categoría del Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
categorias_tienda_4['Producto'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de productos por categoría tienda 4')
plt.xlabel('Categoría del Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# GRAFICO DE LINEAS DE CALIFICACION PROMEDIO POR TIENDA

ingreso_tiendas = {'X': ['tienda_1', 'tienda_2', 'tienda_3', 'tienda_4'], 'Y': [calificacion_tienda_1, calificacion_tienda_2, calificacion_tienda_3, calificacion_tienda_4]}
plt.plot(ingreso_tiendas['X'], ingreso_tiendas['Y'], marker='o', linestyle='-')
# Personalizar el gráfico
plt.xlabel('tienda')
plt.ylabel('calificacion promedio')
plt.title('calificacion promedio de cada tienda')
plt.grid()
plt.show()

# GRAFICOS DE BARRAS DE CANTIDAD DE VENTAS POR PRODUCTO

plt.figure(figsize=(10, 6))
ventas_tienda_1.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de ventas por producto tienda 1')
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
ventas_tienda_2.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de ventas por producto tienda 2')
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
ventas_tienda_3.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de ventas por producto tienda 3')
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 6))
ventas_tienda_4.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Cantidad de ventas por producto tienda 4')
plt.xlabel('Producto')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()