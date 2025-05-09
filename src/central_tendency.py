from pandas import Series
import pandas as pd
import matplotlib.pyplot as plt

class Central_Tendency:
    def __init__(self, serie: Series):
        self.serie = serie
        self.mean = serie.mean()
        self.median = serie.median()
        self.mode = serie.mode().tolist()
        self.variance = serie.var()
        self.standard_deviation = serie.std()

    def plot_central_tendency(self):
        """Genera una gráfica de densidad con líneas para la media, mediana y moda."""
        plt.figure(figsize=(10, 6))
        self.serie.plot(kind='kde', color='lightblue', linewidth=2, label='Densidad')

        # Línea para la media
        plt.axvline(self.mean, color='red', linestyle='--', linewidth=2, label=f'Media: {self.mean:.2f}')
        
        # Línea para la mediana
        plt.axvline(self.median, color='green', linestyle='-', linewidth=2, label=f'Mediana: {self.median:.2f}')
        
        # Líneas para la moda (puede haber múltiples valores)
        for m in self.mode:
            plt.axvline(m, color='blue', linestyle=':', linewidth=2, label=f'Moda: {m:.2f}')

        plt.title('Medidas de Tendencia Central (Densidad)', fontsize=14)
        plt.xlabel('Valores', fontsize=12)
        plt.ylabel('Densidad', fontsize=12)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plot_variance_and_std(self):
        """Genera una gráfica de densidad para la varianza y la desviación estándar."""
        plt.figure(figsize=(10, 6))
        x = ['Varianza', 'Desviación Estándar']
        y = [self.variance, self.standard_deviation]

        # Gráfica de montaña
        plt.fill_between(x, y, color='purple', alpha=0.5, label='Valores')
        plt.plot(x, y, color='purple', linewidth=2)

        for i, v in enumerate(y):
            plt.text(i, v + 0.01, f'{v:.2f}', ha='center', fontsize=12)

        plt.title('Varianza y Desviación Estándar (Montaña)', fontsize=14)
        plt.ylabel('Valor', fontsize=12)
        plt.tight_layout()
        plt.legend()
        plt.show()

    def __str__(self):
        return (
            f"Resultados de las tendencias centrales:\n"
            f"Media: {self.mean}\n"
            f"Mediana: {self.median}\n"
            f"Moda: {self.mode}\n"
            f"Varianza: {self.variance}\n"
            f"Desviación estándar: {self.standard_deviation}\n"
        )