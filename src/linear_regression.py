from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from utils.get_salaries_mean import get_salaries_mean
from pandas import DataFrame
from numpy import sqrt
from matplotlib import pyplot as plt
import seaborn as sns


class Multiple_Linear_Regression:
    def __init__(self, DATA: DataFrame) -> None:
        DATA["Salary"] = get_salaries_mean(DATA)
        self.df = DATA

        self.x = DATA[["Company Score"]]
        self.y = DATA["Salary"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.2, random_state=42)

        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

        self.y_pred = self.model.predict(self.X_test)

        self.mean_squared_error = mean_squared_error(self.y_test, self.y_pred)
        self.r2_score = r2_score(self.y_test, self.y_pred)


    def __str__(self):
        lines: list[str] = [
            f"Coeficientes: {self.model.coef_}",
            f"Intercepción: {self.model.intercept_}",
            f"Error cuadrático medio (MSE): {self.mean_squared_error}",
            f"R^2 Score: {self.r2_score}"
        ]
        return "\n".join(lines)


    def show_real_vs_predict(self):
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=self.y_test, y=self.y_pred, color='blue')
        plt.plot([self.y.min(), self.y.max()], [self.y.min(), self.y.max()], 'r--')
        plt.xlabel('Valor real')
        plt.ylabel('Valor predicho')
        plt.title('Real vs Predicción')
        plt.tight_layout()
        plt.show()


    def show_waste(self):
        residuos = self.y_test - self.y_pred
        plt.figure(figsize=(6, 4))
        sns.histplot(residuos, kde=True, color='purple')
        plt.title('Distribución de residuos')
        plt.xlabel('Error (residuo)')
        plt.tight_layout()
        plt.show()


    def show_relation(self):
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        sns.scatterplot(x=self.x, y=self.y, ax=axes[0])
        axes[0].set_title('x1 vs y')

        sns.scatterplot(x=self.x, y=self.y, ax=axes[1])
        axes[1].set_title('x2 vs y')

        plt.tight_layout()
        plt.show()


    def show_graphics(self):
        self.show_real_vs_predict()
        self.show_waste()


class Simple_Linear_Regression:
    def __init__(self, DATA: DataFrame) -> None:
        # Preprocesamiento de datos
        DATA["Salary"] = get_salaries_mean(DATA)
        self.df = DATA

        # Variables independientes y dependientes
        self.x = self.df[["Company Score"]]  # Cambia esto si necesitas más variables independientes
        self.y = self.df["Salary"]

        # Dividir los datos en entrenamiento y prueba
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.3, random_state=42)

        # Crear y entrenar el modelo de regresión lineal
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)

        # Predicciones
        self.y_pred = self.model.predict(self.X_test)

        # Métricas
        self.rmse = sqrt(mean_squared_error(self.y_test, self.y_pred))
        self.r2 = r2_score(self.y_test, self.y_pred)

        # Coeficientes
        self.intercept = self.model.intercept_
        self.slope = self.model.coef_[0]

    def __str__(self) -> str:
        lines = [
            "Resultados del modelo de Regresión Lineal:",
            f"Intercepto (β0): {self.intercept:.4f}",
            f"Pendiente (β1): {self.slope:.4f}",
            f"RMSE: {self.rmse:.4f}",
            f"R²: {self.r2:.4f}"
        ]
        return "\n".join(lines)

    def show_graphics(self) -> None:
        # Visualización de los datos y la línea de regresión
        plt.figure(figsize=(8, 6))
        plt.scatter(self.X_test, self.y_test, color="blue", label="Datos reales")
        plt.plot(self.X_test, self.y_pred, color="red", label="Línea de regresión")
        plt.xlabel("Company Score")  # Cambia esto según la variable independiente
        plt.ylabel("Salary")
        plt.title("Regresión Lineal - Predicción de Salarios")
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == "__main__":
    from utils.get_final_db import get_final_db
    df = get_final_db()

    simple_linear_regression = Simple_Linear_Regression(df)
    print(simple_linear_regression.__str__())
    simple_linear_regression.show_graphics()

    multiple_linear_regression = Multiple_Linear_Regression(df)
    print(multiple_linear_regression.__str__())
    multiple_linear_regression.show_graphics()
