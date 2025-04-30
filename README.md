# data-science-final-project

## Iniciar el proyecto

### Hacer un fork del repositorio

- Ve a https://github.com/diegodev18/data-science-final-project
- Haz clic en el botón "Fork" en la esquina superior derecha de la página.

### Clonar tu fork del repositorio

```bash
git clone git@github.com:<your_username>/data-science-final-project.git
```

> Recuerda que debes usar SSH para clonar el repositorio y poder contribuir al proyecto.

### Crear un entorno virtual con:

#### Windows

```bash
py -m venv .env
```

#### macOS/Linux

```bash
python3 -m venv .env
```

### Entra en el entorno virtual

#### Windows

```bash
.env\Scripts\activate
```

#### macOS/Linux

```bash
source .env/bin/activate
```

### Instalar las dependencias

#### Windows

```bash
pip install -r requirements.txt
```

#### macOS/Linux

```bash
pip3 install -r requirements.txt
```

### Descargar el dataset

#### Windows

```bash
py download_db.py
```

#### macOS/Linux

```bash
python3 download_db.py
```

### Ejecutar el proyecto

#### Windows

```bash
python src/main.py
```

#### macOS/Linux

```bash
python3 src/main.py
```
