"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_11():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
          c0       c4
     0     0    b,f,g
     1     1    a,c,f
     2     2  a,c,e,f
     3     3      a,b
     ...
     37   37  a,c,e,f
     38   38      d,e
     39   39    a,d,f
    """
    
    # Cargar el archivo tbl1.tsv en un DataFrame
    df = pd.read_csv('files/input/tbl1.tsv', sep='\t')
    
    # Agrupar por la columna c0 y aplicar la función lambda que convierte a string y une con ','
    df_grouped = df.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(x.astype(str)))).reset_index()
    
    return df_grouped

print(pregunta_11()) #imprime la funcion