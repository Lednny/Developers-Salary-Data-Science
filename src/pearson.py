from pandas import Series, DataFrame
from scipy.stats import pearsonr
from seaborn import heatmap
from numpy import polyfit
import matplotlib.pyplot as plt


def valid_cols(col1, col2):
    if not isinstance(col1, Series) or not isinstance(col2, Series):
        raise ValueError("One or both columns are not Series.")


class Pearson_Correlation:
    def __init__(self, col1, col2):
        valid_cols(col1, col2)

        self.col1: Series = col1
        self.col2: Series = col2
        self.corr, self.p_value = pearsonr(self.col1, self.col2)


    def calculate(self) -> float:
        return self.col1.corr(self.col2)


    def __str__(self) -> str:
        return f"Coeficiente de correlación de Pearson: {self.corr:.4f}\nValor p: {self.p_value:.4e}"


    def show_graphics(self) -> bool:
        plt.figure(figsize=(8,6))
        plt.scatter(self.col1, self.col2, color='blue', label='Datos')
        m, b = polyfit(self.col1, self.col2, 1)  # línea de tendencia
        plt.plot(self.col1, m * self.col1 + b, color='red', label='Línea de regresión')
        plt.title(f"Correlación de Pearson: {self.corr:.2f}")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        return True


    def show_heat_map(self):
        data = DataFrame(
            [[1, self.corr], [self.corr, 1]],
            index=['col1', 'col2'],
            columns=['col1', 'col2']
        )
        plt.figure(figsize=(6, 5))
        heatmap(data, annot=True, cmap='coolwarm', center=0, linewidths=0.5)
        plt.title('Matriz de Correlacion de Pearson')
        plt.show()


if __name__ == '__main__':
    from utils.get_final_db import get_final_db
    from utils.get_salaries_mean import get_salaries_mean
    df = get_final_db()
    salaries = get_salaries_mean(df)
    pearson = Pearson_Correlation(df['Company Score'], salaries)
    print(pearson.__str__())
    pearson.show_graphics()
    pearson.show_heat_map()
