from utils.get_good_or_bad_companies import get_good_or_bad_companies
from utils.get_salaries_mean import get_salaries_mean
from pandas import DataFrame
import matplotlib.pyplot as plt


class Exploratory_Analysis:
    def __init__(self, df: DataFrame):
        self.df = df.copy()
        self.df['Salary'] = get_salaries_mean(df)
        print("Columnas disponibles en el DataFrame después de la limpieza:", self.df.columns)
        self.cols = self.df.columns.tolist()
        self.descriptive_stats = self.df.describe(include='all')
        self.top_titles = self.df.groupby('Job Title')['Salary'].mean()
        self.top_locations = self.df.groupby('Location')['Salary'].mean()
        self.companies_scores = self.df.groupby('Company')['Company Score'].mean()
        self.top_companies = get_good_or_bad_companies(self.df['Company'], self.df['Company Score'])


    def __str__(self):
        lines: list[str] = [
            f"Columnas disponibles: {', '.join(self.cols)}",
            f"Estadísticas descriptivas:\n{self.descriptive_stats}",
            f"Promedio de salarios por título:\n{self.top_titles}",
            f"Promedio de salarios por ubicación:\n{self.top_locations}",
            f"Empresas con buenos puntajes:\n{", ".join(self.top_companies['good']['companies'][:10])}...",
            f"Empresas con malos puntajes:\n{", ".join(self.top_companies['bad']['companies'][:10])}..."
        ]
        return '\n\n'.join(lines)


    def run_analysis(self) -> str:
        lines: list[str] = [
            "\nEjecutando análisis...\n",
            self.highest_paying_remote_jobs(),
            self.best_countries_for_software_engineers(),
            self.location_salary_analysis(),
            self.salary_low_rating_companies(),
            self.salary_variation_analysis(),
            self.employment_types_in_high_rated_companies()
        ]
        return '\n\n'.join(lines)


    # Pregunta 1: ¿Qué títulos de trabajo remoto ofrecen los salarios más altos?
    def highest_paying_remote_jobs(self) -> str:
        top_jobs = self.df.groupby('Job Title')['Salary'].mean().sort_values(ascending=False).head(10)

        # Gráfica de barras
        plt.figure(figsize=(10, 6))
        top_jobs.plot(kind='bar', color='skyblue')
        plt.title('Títulos de trabajo remoto con los salarios más altos', fontsize=14)
        plt.xlabel('Título de trabajo', fontsize=12)
        plt.ylabel('Salario promedio', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        return f"Títulos de trabajo remoto con los salarios más altos:\n{top_jobs}"


    # Pregunta 2: ¿Qué ciudades de EUA ofrecen mejores salarios para empleos remotos en ingeniería de software?
    def best_countries_for_software_engineers(self) -> str:
        if 'Location' not in self.df.columns:
            return "best_countries_for_software_engineers: Error: La columna 'Location' no está presente en el DataFrame."
        is_software_engineer = self.df['Job Title'].str.contains('engineer', case=False, na=False)
        top_countries = self.df[is_software_engineer].groupby('Location')['Salary'].mean().sort_values(ascending=False).head(10)

        # Gráfica de barras
        plt.figure(figsize=(10, 6))
        top_countries.plot(kind='bar', color='orange')
        plt.title('Ciudades de EUA con mejores salarios para ingenieros de software', fontsize=14)
        plt.xlabel('País', fontsize=12)
        plt.ylabel('Salario promedio', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        return f"Ciudades de EUA con mejores salarios para empleos remotos en ingeniería de software:\n{top_countries}"

    # Pregunta 3: ¿Cuáles son las ubicaciones más comunes para trabajos remotos y cómo varían los salarios entre ellas?
    def location_salary_analysis(self) -> str:
        if 'Location' not in self.df.columns:
            return "location_salary_analysis: Error: La columna 'Location' no está presente en el DataFrame."
        filtered_df = self.df[~self.df['Location'].isin(['EUA', 'Remote'])]
        if filtered_df.empty:
            return "location_salary_analysis: Error: No hay datos después de filtrar las ubicaciones 'EUA' y 'Remote'."
        common_locations = filtered_df['Location'].value_counts().head(10)
        salary_by_location = filtered_df.groupby('Location')['Salary'].mean().sort_values(ascending=False)

        if "United States" in common_locations:
            del common_locations["United States"]

        # Gráfica de barras
        plt.figure(figsize=(10, 6))
        common_locations.plot(kind='bar', color='green')
        plt.title('Ubicaciones más comunes para trabajos remotos', fontsize=14)
        plt.xlabel('Ubicación', fontsize=12)
        plt.ylabel('Cantidad de trabajos', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

        return f"Ubicaciones más comunes para trabajos remotos:\n{common_locations}\n\nSalarios promedio por ubicación:\n{salary_by_location}"


    # Pregunta 4: ¿Qué tan competitivos son los salarios en trabajos remotos de empresas con baja calificación?
    def salary_low_rating_companies(self) -> str:
        if 'Company Score' not in self.df.columns or 'Salary' not in self.df.columns:
            return "salary_low_rating_companies: Error: Las columnas 'Company Score' o 'Salary' no están presentes en el DataFrame."
        low_rating_companies = self.df[self.df['Company Score'] < 3]
        avg_salary = low_rating_companies['Salary'].mean()

        # Gráfica de barras
        plt.figure(figsize=(6, 4))
        plt.bar(['Empresas con baja calificación'], [avg_salary], color='red')
        plt.title('Salario promedio en empresas con baja calificación', fontsize=14)
        plt.ylabel('Salario promedio', fontsize=12)
        plt.tight_layout()
        plt.show()

        return f"Salario promedio en empresas con baja calificación: {avg_salary}"


    # Pregunta 5: ¿Los salarios en trabajos remotos varían más según la ubicación o según la empresa?
    def salary_variation_analysis(self) -> str:
        if 'Location' not in self.df.columns or 'Company' not in self.df.columns:
            return "salary_variation_analysis: Error: Las columnas 'Location' o 'Company' no están presentes en el DataFrame."
        variation_by_location = self.df.groupby('Location')['Salary'].std().mean()
        variation_by_company = self.df.groupby('Company')['Salary'].std().mean()

        # Gráfica de barras
        plt.figure(figsize=(6, 4))
        plt.bar(['Ubicación', 'Empresa'], [variation_by_location, variation_by_company], color=['blue', 'purple'])
        plt.title('Variación promedio de salarios', fontsize=14)
        plt.ylabel('Variación promedio', fontsize=12)
        plt.tight_layout()
        plt.show()

        return f"Variación promedio de salarios por ubicación: {variation_by_location}\nVariación promedio de salarios por empresa: {variation_by_company}"


    # Pregunta 6: ¿Qué tipos de empleo remoto (full-time, contract, freelance) predominan en empresas con alta calificación?
    def employment_types_in_high_rated_companies(self) -> str:
        if 'Company Score' not in self.df.columns or 'Job Title' not in self.df.columns:
            return "employment_types_in_high_rated_companies: Error: Las columnas 'Company Score' o 'Job Title' no están presentes en el DataFrame."
        high_rated_companies = self.df[self.df['Company Score'] >= 4]
        employment_type_counts = high_rated_companies['Job Title'].value_counts().head(10)

        # Gráfica circular mejorada
        plt.figure(figsize=(8, 8))
        employment_type_counts.plot(
            kind='pie',
            autopct='%1.1f%%',
            startangle=140,
            colors=['gold', 'lightblue', 'lightgreen', 'coral', 'violet', 'cyan', 'pink', 'gray', 'brown', 'purple'],
        )
        plt.title('Distribución de tipos de empleo en empresas con alta calificación (Top 10)', fontsize=14)
        plt.ylabel('')
        plt.tight_layout()
        plt.show()

        return f"Tipos de empleo remoto predominantes en empresas con alta calificación:\n{employment_type_counts}"


if __name__ == "__main__":
    from utils.get_final_db import get_final_db
    df = get_final_db()

    exploratory = Exploratory_Analysis(df)
    exploratory.location_salary_analysis()
    # print(exploratory.__str__())
    # print(exploratory.run_analysis())
