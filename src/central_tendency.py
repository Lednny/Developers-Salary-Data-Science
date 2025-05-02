import pandas as pd

def central_tendency(serie, imprimir=True):
    if not isinstance(serie, pd.Series):
        serie = pd.Series(serie)
    
    result = {
        "media": serie.mean(),
        "mediana": serie.median(),
        "moda": serie.mode().tolist(), 
        "varianza": serie.var(),
        "desviacion_estandar": serie.std()
    }
    
    if imprimir:
        print("Resultados de las tendcias centrales: ")
        print(result)
    
    return result

