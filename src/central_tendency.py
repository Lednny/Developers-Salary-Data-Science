import pandas as pd

def central_tendency(serie):
    if not isinstance(serie, pd.Series):
        serie = pd.Series(serie)
    return {
        "media": serie.mean(),
        "mediana": serie.median(),
        "moda": serie.mode().tolist()
    }
