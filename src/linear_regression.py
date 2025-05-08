import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from utils.get_salaries_mean import get_salaries_mean


class Linear_Regression:
    def __init__(self, DATA: pd.DataFrame) -> None:
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
        self.rmse = np.sqrt(mean_squared_error(self.y_test, self.y_pred))
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
    linear_regression = Linear_Regression(df)
    print(linear_regression.__str__())
    linear_regression.show_graphics()
