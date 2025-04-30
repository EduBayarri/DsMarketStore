

pip install pandas matplotlib

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from itertools import cycle

from google.colab import drive
drive.mount('/content/drive')

import time
start_time = time.time()

df_sales = pd.read_csv("/content/drive/MyDrive/Proyecto DSMarket/DSMarket/data_dsmarket/item_sales.csv")
df_eventos = pd.read_csv("/content/drive/MyDrive/Proyecto DSMarket/DSMarket/data_dsmarket/daily_calendar_with_events.csv")
df_prices = pd.read_csv("/content/drive/MyDrive/Proyecto DSMarket/DSMarket/data_dsmarket/item_prices.csv")
print('Se han cargado los datos iniciales')

df_sales.head()

df_eventos.head()

df_prices.head()

df_sal = df_sales.copy()

#Con esta secuencia creamos un registro por cada dia de venta de un producto almacenando el dia
#en la variable d y la venta en la variable ventas.
df_sal = pd.melt(df_sal, id_vars=['id','item','category','department','store','store_code','region'], var_name='d', value_name='ventas')

#Las variables tipo object las pasamos a category para que tengan menos peso en memoria
df_sal['id']=df_sal['id'].astype('category')
df_sal['store']=df_sal['store'].astype('category')
df_sal['region']=df_sal['region'].astype('category')
df_sal['d']=df_sal['d'].astype('category')

print('Se ha transformado el DataFrame de ventas')

df_sal

df_pri = df_prices.copy()

#Eliminamos valores duplicados
df_pri.drop_duplicates(inplace=True)

#Volvemos a indexar el dataset
df_pri.reset_index(drop=True,inplace=True)

#Guardamos los valores nulos
nulos = df_pri['yearweek'].isna()

#Rellenamos los nulos con el valor anterior
df_pri['yearweek'] = df_pri['yearweek'].ffill()

#A los nulos que tenimaos guardados le sumamos 1
df_pri.loc[nulos, 'yearweek'] += 1

#Sumamos 1 a la semana para que el año empiece desde la semana 1 en vez de la semana 0
df_pri['yearweek'] = df_pri['yearweek']+1


df_pri['yearweek']=df_pri['yearweek'].astype('str')


df_pri['año'] = df_pri['yearweek'].str[:4].astype(int)
df_pri['semana'] = df_pri['yearweek'].str[4:6].astype(int)

#Eliminamos los registros donde la semana es 54 ya que son pocos y los podemos tomar como datos falsos
df_pri = df_pri[df_pri['semana'] != 54]


#Redondeamos la variable sell_price a dos decimales ya que cada registro tenia una
#cantidad de decimales distintos, así estandarizamos los decimales
df_pri['sell_price'] = df_pri['sell_price'].round(2)

#Generamos la variable id para poder cruzar con el dataframe de ventas
df_pri['id']=df_pri['item']+'_'+df_pri['store_code']


df_pri['id']=df_pri['id'].astype('category')
df_pri['semana']=df_pri['semana'].astype('category')
df_pri['año']=df_pri['año'].astype('category')


# Nuevo orden de las columnas
orden_columns = ['id','item','category','store_code','yearweek','año','semana','sell_price']

# Reordenar el DataFrame usando reindex
df_pri = df_pri.reindex(columns=orden_columns)

print('Se ha transformado el DataFrame de precios')

df_pri.info()

df_pri

df_eve = df_eventos.copy()

#Los nulos de la variable event se rellenan con el valor 'Sin Evento'
df_eve['event']= df_eve['event'].fillna('Sin_Evento')

df_eve['date'] = pd.to_datetime(df_eve['date'],format='%Y-%m-%d')

df_eve['d']=df_eve['d'].astype('category')
df_eve['event']=df_eve['event'].astype('category')

#df_eve = df_eve.drop(columns=['weekday','weekday_int'])

print('Se ha transformado el DataFrame de calendario')

df_eve

#Unimos los DataFrames de Ventas y calendario
df_item = pd.merge(df_sal,df_eve, on ='d', how = 'inner')

print('Se han unido los DataFrames de Ventas y calendario')

df_item

df_item['año'] = df_item['date'].dt.isocalendar().year
df_item['semana'] = df_item['date'].dt.isocalendar().week
df_item['semana'] = df_item['semana'].astype('category')
df_item['año'] = df_item['año'].astype('category')


df_item['trimestre'] = df_item['date'].dt.quarter

df_item[df_item['id'] == 'ACCESORIES_1_001_NYC_1']

df_item.info()

df_pri

df_item.head()

df_item = df_item.drop(columns=['d','date','weekday','weekday_int'])

# Convertir todas las columnas de tipo object a category
df_item = df_item.apply(lambda col: col.astype('category') if col.dtype == 'object' else col)

for col in df_item.select_dtypes(include=['int']):
    df_item[col] = pd.to_numeric(df_item[col], downcast='integer')

for col in df_item.select_dtypes(include=['float']):
  df_item[col] = pd.to_numeric(df_item[col], downcast='float')

df_item.info()

def evento_func(data):
    evento_distinto = data[data != 'Sin_Evento']
    return evento_distinto.iloc[0] if not evento_distinto.empty else 'Sin_Evento'

df_item = df_item.groupby(
    ['id', 'item', 'category', 'department', 'store', 'store_code', 'region', 'año', 'semana', 'trimestre'],observed=True
).agg({
    'event': evento_func, # Mantener el primer evento distinto de 'Sin_Evento'
    'ventas': 'sum'  # Sum the sales by week
}).reset_index()

df_item.sort_values(by=['id','año','semana'])

#Hacemos left join con el df de precios para no perder registros, despues se trataran los nulos que aparecen

df_agrupado = pd.merge(df_item,df_pri,on=['id','año','semana'],how='left')

df_agrupado.info()

df_agrupado.isnull().sum()

df_agrupado = df_agrupado.drop(columns=['item_y','category_y','store_code_y'])

df_agrupado['yearweek'] = df_agrupado['yearweek'].fillna(df_agrupado['año'].astype(str) + df_agrupado['semana'].astype(str).str.zfill(2))

df_agrupado['yearweek'].unique()

df_agrupado['yearweek'] = df_agrupado['yearweek'].astype(str).str.replace('.0', '', regex=False)

df_agrupado['yearweek'].unique()

df_agrupado.isnull().sum()



df_agrupado['sell_price'][(df_agrupado['id'] == 'ACCESORIES_1_001_NYC_1')].unique()

df_agrupado.describe()

df_agrupado.sort_values(by=['item_x', 'año','semana'],inplace=True)

df_agrupado['sell_price'] =df_agrupado.groupby(['item_x','store_code_x'])['sell_price'].ffill()

df_agrupado['sell_price'] =df_agrupado.groupby(['item_x','store_code_x'])['sell_price'].bfill()

df_agrupado.isnull().sum()

df_agrupado = df_agrupado.rename(columns={'item_x': 'item', 'category_x': 'category', 'store_code_x': 'store_code'})

df_agrupado.sort_values(by=['año', 'semana', 'region','store_code','department',],inplace=True)

df_agrupado.info()

df_agrupado.reset_index(drop=True, inplace=True)

df_agrupado.head()

df_agrupado['yearweek'] = df_agrupado['yearweek'].astype(int)

# Convertir todas las columnas de tipo object a category
df_agrupado = df_agrupado.apply(lambda col: col.astype('category') if col.dtype == 'object' else col)

#Convertir las variables al tipo de dato menos pesado posible
for col in df_agrupado.select_dtypes(include=['int']):
    df_agrupado[col] = pd.to_numeric(df_agrupado[col], downcast='integer')

for col in df_agrupado.select_dtypes(include=['float']):
  df_agrupado[col] = pd.to_numeric(df_agrupado[col], downcast='float')

df_agrupado.info()

df_agrupado[df_agrupado['id']=='ACCESORIES_1_001_NYC_1']

df_agrupado.info()

df_agrupado.to_csv('/content/drive/MyDrive/Proyecto DSMarket/DSMarket/DatosAgrupadosEnSemanas.csv.gz', index=False, compression='gzip')

end_time = time.time()
execution_time = end_time - start_time
print("El NoteBook tarda:", execution_time/60, "minutos en ejecutarse")