
import pandas as pd

###Función para calcular el porcentaje de nulos###
def porcentaje_nulos(df):
    nulos = df.isnull().sum()
    porcentaje = (nulos / len(df)) * 100
    return pd.DataFrame({'nulos': nulos, 'porcentaje': porcentaje}).sort_values(by='porcentaje', ascending=False)