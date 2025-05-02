from pandas import DataFrame, Series
from utils.get_salaries_mean import get_salaries_mean


def get_good_or_bad_companies(companies, scores, bad_threshold: int = 3) -> dict[str, dict[str, list[str]]]:
    if not isinstance(companies, Series) or not isinstance(scores, Series):
        raise TypeError("Companies and scores must be pandas Series")

    stats = { 'good': { 'companies': [], 'length': 0 }, 'bad': { 'companies': [], 'length': 0 } }
    for company, score in zip(companies, scores):
        if score > bad_threshold:
            stats['good']['companies'].append(company)
            stats['good']['length'] += 1
            continue;
        stats['bad']['companies'].append(company)
        stats['bad']['length'] += 1
    return stats


class Exploratory_Analysis:
    def __init__(self, df: DataFrame):
        self.df = df
        self.cols = df.columns.tolist()
        self.descriptive_stats = self.df.describe(include='all')
        self.salary = get_salaries_mean(self.df)
        self.top_titles = self.salary.groupby(df['Job Title']).mean() # Paises por título
        self.top_locations = self.salary.groupby(df['Location']).mean() # Paises por ubicación
        self.companies_scores = self.df['Company'].groupby(df['Company Score'])
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


"""
def analizar_datos(df: DataFrame):
    print("Columnas disponibles:", df.columns.tolist())

    # Estadísticas descriptivas
    print("\nEstadísticas descriptivas:\n", df.describe(include='all'))

    # 1. Títulos de trabajo con mayores salarios
    print("\n1. Títulos de trabajo con mayores salarios:")
    top_titles = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)
    print(top_titles)

    # 2. Países con mejores salarios en ingeniería de software
    print("\n2. Países con mejores salarios para empleos remotos en ingeniería de software:")
    software_jobs = df[df['job_title'].str.contains("software", case=False)]
    top_countries = software_jobs.groupby('employee_residence')['salary_in_usd'].mean().sort_values(ascending=False).head(10)
    print(top_countries)

    # 3. Ubicaciones más comunes y salarios
    print("\n3. Ubicaciones más comunes para trabajos remotos:")
    ubicaciones = df['employee_residence'].value_counts().head(10)
    print(ubicaciones)

    print("\nSalarios promedio por ubicación:")
    salarios_por_ubicacion = df.groupby('employee_residence')['salary_in_usd'].mean().sort_values(ascending=False).head(10)
    print(salarios_por_ubicacion)

    # 4. Empresas grandes con baja calificación
    if 'Company Score' in df.columns and 'company_size' in df.columns:
        print("\n4. Salarios en empresas grandes con baja calificación (< 3.0):")
        filtro = (df['Company Score'] < 3.0) & (df['company_size'].isin(['Large', 'Enterprise']))
        empresas_filtradas = df[filtro]
        print("Salario medio:", empresas_filtradas['salary_in_usd'].mean())
        print("Cantidad de registros:", len(empresas_filtradas))
    else:
        print("No hay columnas 'Company Score' o 'company_size'.")

    # 5. Variación salarial: ubicación vs tamaño empresa
    if 'company_size' in df.columns:
        print("\n5. ¿Varían más los salarios por ubicación o tamaño de empresa?")
        var_por_ubicacion = df.groupby('employee_residence')['salary_in_usd'].var().mean()
        var_por_empresa = df.groupby('company_size')['salary_in_usd'].var().mean()
        print("Varianza promedio por ubicación:", var_por_ubicacion)
        print("Varianza promedio por tamaño de empresa:", var_por_empresa)
    else:
        print("No hay columna 'company_size'.")

    # 6. Tipos de empleo en empresas con alta calificación
    if 'Company Score' in df.columns and 'employment_type' in df.columns:
        print("\n6. Tipos de empleo en empresas con alta calificación (>= 4.0):")
        top_empresas = df[df['Company Score'] >= 4.0]
        tipos = top_empresas['employment_type'].value_counts()
        print(tipos)
    else:
        print("No hay columnas 'Company Score' o 'employment_type'.")
"""


if __name__ == "__main__":
    from utils.get_final_db import get_final_db
    df = get_final_db()

    exploratory = Exploratory_Analysis(df)
    print(exploratory.__str__())
    # exploratory.create_descriptive_stats_csv()
