import pandas as pd

def central_tendency():
    media = serie.mean()
    mediana = serie.median()
    moda = serie.mode().tolist()

    return {
        "media": media,
        "mediana": mediana,
        "moda": moda,
    }
