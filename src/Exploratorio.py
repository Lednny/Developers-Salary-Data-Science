import pandas as pd
import os
import sys
from clear_db import clear_db
from external.json_db_path import get_file_with_saved_path_content

def cargar_datos_limpios():
    DB_PATH = get_file_with_saved_path_content()

    if not DB_PATH or not os.path.exists(DB_PATH):
        print('No existe la base de datos. Descárgala con el script "download_db.py".')
        sys.exit(-1)

    CLEANED_DB_PATH = clear_db(DB_PATH)
    if not CLEANED_DB_PATH:
        sys.exit(-1)

    df = pd.read_csv(CLEANED_DB_PATH)
    return df

def analizar_datos(df):
    print("Columnas disponibles:", df.columns.tolist())

    # Estadísticas descriptivas
    print("\nEstadísticas descriptivas:\n", df.describe(include='all'))

    # Medidas de tendencia central y dispersión
    salario = df['salary_in_usd']
    print("\nMedidas de tendencia central y dispersión:")
    print("Media:", salario.mean())
    print("Mediana:", salario.median())
    print("Moda:", salario.mode().iloc[0])
    print("Varianza:", salario.var())
    print("Desviación estándar:", salario.std())

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

if __name__ == "__main__":
    df = cargar_datos_limpios()
    analizar_datos(df)

