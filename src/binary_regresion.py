import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
from utils.get_salaries_mean import get_salaries_mean


class Binary_Regression:
    def __init__(self, DATA: pd.DataFrame) -> None:
        DATA["Salary"] = get_salaries_mean(DATA)
        self.df = DATA

        self.df["Date_encoded"] = self.df["Date"].astype(str).apply(lambda x: 0 if "day" in x and int(x.split("d")[0]) <= 7 else 1)

        self.median_salary = self.df["Salary"].median()
        self.high_salary = (self.df["Salary"] > self.median_salary).astype(int)

        self.df["High_Salary"] = self.high_salary
        self.df["Company_encoded"] = LabelEncoder().fit_transform(self.df["Company"])

        self.x = self.df[["Company Score", "Date_encoded", "Company_encoded"]]
        self.y = self.df["High_Salary"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.3, random_state=42)

        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)

        self.y_pred = self.model.predict(self.X_test)
        self.y_prob = self.model.predict_proba(self.X_test)[:,1]

        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred)
        self.classification_report = classification_report(self.y_test, self.y_pred)
        self.roc_auc_score = roc_auc_score(self.y_test, self.y_prob)

        self.fpr, self.tpr, _ = roc_curve(self.y_test, self.y_prob)


    def __str__(self) -> str:
        lines = [
            "Matriz de confusion:",
            f"{self.confusion_matrix}",
            "\nReporte de clasificación:",
            f"{self.classification_report}"
            f"ROC AUC Score: {roc_auc_score:.4f}"
        ]
        return "\n".join(lines)


    def show_graphics(self) -> None:
        plt.figure(figsize=(8, 6))
        plt.plot(self.fpr, self.tpr, label="Regresión Logística (AUC = {:.2f})".format(roc_auc_score(self.y_test, self.y_prob)))
        plt.plot([0,1],[0,1],'k--')
        plt.xlabel("Tasa de falsos positivos")
        plt.ylabel("Tasa de verdaderos positivos")
        plt.title("Curva ROC - Predicción de salarios altos")
        plt.legend(loc="lower right")
        plt.grid()
        plt.show()


if __name__ == "__main__":
    from utils.get_final_db import get_final_db
    df = get_final_db()
    binary_regression = Binary_Regression(df)
    print(binary_regression.__str__())
    binary_regression.show_graphics()
