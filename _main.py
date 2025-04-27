import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

tienda_1 = pd.read_csv('./data/tienda_1.csv')
tienda_2 = pd.read_csv('./data/tienda_2.csv')
tienda_3 = pd.read_csv('./data/tienda_3.csv')
tienda_4 = pd.read_csv('./data/tienda_4.csv')


categorias_tienda_1 = tienda_1.groupby('Categoría del Producto')['Precio'].sum()
print(categorias_tienda_1)