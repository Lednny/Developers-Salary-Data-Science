from pandas import DataFrame, Series
from utils.get_salaries_mean import get_salaries_mean
import re
import matplotlib.pyplot as plt

def clean_salary(salary: str) -> float:
    if isinstance(salary, str):
        # Extraer el rango salarial (por ejemplo, "$92K - $116K")
        match = re.findall(r"(\d+)[Kk]", salary)
        if match:
            # Convertir los valores a números y calcular el promedio
            nums = [float(num) * 1000 for num in match]
            return sum(nums) / len(nums)
    return float('nan')

def get_good_or_bad_companies(companies, scores, bad_threshold: int = 3) -> dict[str, dict[str, list[str]]]:
    if not isinstance(companies, Series) or not isinstance(scores, Series):
        raise TypeError("Companies and scores must be pandas Series")

    stats = { 'good': { 'companies': [], 'length': 0 }, 'bad': { 'companies': [], 'length': 0 } }
    for company, score in zip(companies, scores):
        if score > bad_threshold:
            stats['good']['companies'].append(company)
            stats['good']['length'] += 1
            continue
        stats['bad']['companies'].append(company)
        stats['bad']['length'] += 1
    return stats


class Exploratory_Analysis:
    def __init__(self, df: DataFrame):
        self.df = df.copy()
        self.df['Salary'] = self.df['Salary'].apply(clean_salary)
        self.df = self.df.dropna(subset=['Salary'])
        print("Columnas disponibles en el DataFrame después de la limpieza:", self.df.columns)
        self.cols = self.df.columns.tolist()
        self.descriptive_stats = self.df.describe(include='all')
        self.top_titles = self.df.groupby('Job Title')['Salary'].mean()  
        self.top_locations = self.df.groupby('Location')['Salary'].mean()  
        self.companies_scores = self.df.groupby('Company')['Company Score'].mean()  
        self.top_companies = get_good_or_bad_companies(self.df['Company'], self.df['Company Score'])

    def __str__(self):
        lines = [
            f"Columnas disponibles: {', '.join(self.cols)}",
            f"Estadísticas descriptivas:\n{self.descriptive_stats}",
            f"Promedio de salarios por título:\n{self.top_titles}",
            f"Promedio de salarios por ubicación:\n{self.top_locations}",
            f"Empresas con buenos puntajes:\n{self.top_companies['good']['length']}",
            f"Empresas con malos puntajes:\n{self.top_companies['bad']['length']}"
        ]
        return '\n\n'.join(lines)
    
    def run_analysis(self):
        print("")
        print("Ejecutando análisis...")
        print("")
        self.highest_paying_remote_jobs()
        print("")
        self.best_countries_for_software_engineers()
        print("")
        self.location_salary_analysis()
        print("")
        self.salary_low_rating_companies()
        print("")
        self.salary_variation_analysis()
        print("")
        self.employment_types_in_high_rated_companies()
        print("")

    # Pregunta 1: ¿Qué títulos de trabajo remoto ofrecen los salarios más altos?
    def highest_paying_remote_jobs(self):
        top_jobs = self.df.groupby('Job Title')['Salary'].mean().sort_values(ascending=False).head(10)
        print("Títulos de trabajo remoto con los salarios más altos:")
        print(top_jobs)

        # Gráfica de barras
        plt.figure(figsize=(10, 6))
        top_jobs.plot(kind='bar', color='skyblue')
        plt.title('Títulos de trabajo remoto con los salarios más altos', fontsize=14)
        plt.xlabel('Título de trabajo', fontsize=12)
        plt.ylabel('Salario promedio', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    # Pregunta 2: ¿Qué países ofrecen mejores salarios para empleos remotos en ingeniería de software?
    def best_countries_for_software_engineers(self):
        if 'Location' not in self.df.columns:
            print("Error: La columna 'Location' no está presente en el DataFrame.")
            return
        is_software_engineer = self.df['Job Title'].str.contains('engineer', case=False, na=False)
        top_countries = self.df[is_software_engineer].groupby('Location')['Salary'].mean().sort_values(ascending=False).head(10)
        print("Países con mejores salarios para empleos remotos en ingeniería de software:")
        print(top_countries)

        # Gráfica de barras
        plt.figure(figsize=(10, 6))
        top_countries.plot(kind='bar', color='orange')
        plt.title('Países con mejores salarios para ingenieros de software', fontsize=14)
        plt.xlabel('País', fontsize=12)
        plt.ylabel('Salario promedio', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    # Pregunta 3: ¿Cuáles son las ubicaciones más comunes para trabajos remotos y cómo varían los salarios entre ellas?
    def location_salary_analysis(self):
        common_locations = self.df['Location'].value_counts().head(10)
        salary_by_location = self.df.groupby('Location')['Salary'].mean().sort_values(ascending=False)
        print("Ubicaciones más comunes para trabajos remotos:")
        print(common_locations)
        print("\nSalarios promedio por ubicación:")
        print(salary_by_location)

        # Gráfica de barras
        plt.figure(figsize=(10, 6))
        common_locations.plot(kind='bar', color='green')
        plt.title('Ubicaciones más comunes para trabajos remotos', fontsize=14)
        plt.xlabel('Ubicación', fontsize=12)
        plt.ylabel('Cantidad de trabajos', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    # Pregunta 4: ¿Qué tan competitivos son los salarios en trabajos remotos de empresas con baja calificación?
    def salary_low_rating_companies(self):
        if 'Company Score' not in self.df.columns or 'Salary' not in self.df.columns:
            print("Error: Las columnas 'Company Score' o 'Salary' no están presentes en el DataFrame.")
            return
        low_rating_companies = self.df[self.df['Company Score'] < 3]
        avg_salary = low_rating_companies['Salary'].mean()
        print(f"Salario promedio en empresas con baja calificación: {avg_salary}")

        # Gráfica de barras
        plt.figure(figsize=(6, 4))
        plt.bar(['Empresas con baja calificación'], [avg_salary], color='red')
        plt.title('Salario promedio en empresas con baja calificación', fontsize=14)
        plt.ylabel('Salario promedio', fontsize=12)
        plt.tight_layout()
        plt.show()

    # Pregunta 5: ¿Los salarios en trabajos remotos varían más según la ubicación o según la empresa?
    def salary_variation_analysis(self):
        if 'Location' not in self.df.columns or 'Company' not in self.df.columns:
            print("Error: Las columnas 'Location' o 'Company' no están presentes en el DataFrame.")
            return
        variation_by_location = self.df.groupby('Location')['Salary'].std().mean()
        variation_by_company = self.df.groupby('Company')['Salary'].std().mean()
        print(f"Variación promedio de salarios por ubicación: {variation_by_location}")
        print(f"Variación promedio de salarios por empresa: {variation_by_company}")

        # Gráfica de barras
        plt.figure(figsize=(6, 4))
        plt.bar(['Ubicación', 'Empresa'], [variation_by_location, variation_by_company], color=['blue', 'purple'])
        plt.title('Variación promedio de salarios', fontsize=14)
        plt.ylabel('Variación promedio', fontsize=12)
        plt.tight_layout()
        plt.show()

    # Pregunta 6: ¿Qué tipos de empleo remoto (full-time, contract, freelance) predominan en empresas con alta calificación?
    def employment_types_in_high_rated_companies(self):
        if 'Company Score' not in self.df.columns or 'Job Title' not in self.df.columns:
            print("Error: Las columnas 'Company Score' o 'Job Title' no están presentes en el DataFrame.")
            return
        high_rated_companies = self.df[self.df['Company Score'] >= 4]
        employment_type_counts = high_rated_companies['Job Title'].value_counts().head(10)
        print("Tipos de empleo remoto predominantes en empresas con alta calificación:")
        print(employment_type_counts)

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

if __name__ == "__main__":
    from utils.get_final_db import get_final_db
    df = get_final_db()

    exploratory = Exploratory_Analysis(df)
    print(exploratory.__str__())
    exploratory.run_analysis()