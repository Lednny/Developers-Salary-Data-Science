from pandas import Series


class Central_Tendency:
    def __init__(self, serie: Series):
        self.serie = serie
        self.mean = serie.mean()
        self.median = serie.median()
        self.mode = serie.mode().tolist()
        self.variance = serie.var()
        self.standard_deviation = serie.std()


    def __str__(self):
        return f"Resultados de las tendencias centrales:\nMedia: {self.mean}\nMediana: {self.median}\nModa: {self.mode}\nVarianza: {self.variance}\nDesviación estándar: {self.standard_deviation}\n"
