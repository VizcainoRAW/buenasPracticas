# Flask CRUD ORM

Este proyecto tiene como objetivo poner en práctica las mejores prácticas de desarrollo con Flask y SQLAlchemy.

## Instalación

Asegúrate de tener Python y pip instalados en tu sistema. Luego, sigue estos pasos:

### Clonar el repositorio

Puedes clonar el repositorio utilizando HTTPS con el siguiente comando:

```bash
git clone https://github.com/VizcainoRAW/buenasPracticas.git
cd buenasPracticas/flask_python
```

o descarga https://github.com/VizcainoRAW/buenasPracticas/tree/main/flask_python


### Crea un entorno virtual (opcional pero recomendado)

```bash
pip install virtualenv
python -m venv env
source env/bin/activate  # En sistemas Unix/Linux
env\Scripts\activate  # En Windows
```

### Instala las dependencias del proyecto:

```bash
pip install -r flask_crud_orm/requirements.txt
```

Se va a correr la base de datos en host local(puede ser cambiado a conveniencia):
en flask_crud_orm estan tasksDB.sql y tasksDB_records.sql, tienen que ser ejecutadas todas las lineas de comando con MySQL, siendo el script para montar la base de datos y sus resgistros de testing(para esto tiene que estar instalado MySQL Server).

## Configuración
Antes de ejecutar el proyecto, asegúrate de que la configuración de la base de datos sea correcta. En el archivo flask_crud_orm/app/config.py, verifica que los valores de usuario, contraseña, host, puerto y nombre de la base de datos coincidan con tu configuración. Por defecto se encuentran como:

    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': '3306',
    'database': 'TasksDB'

## Ejecución
Para ejecutar el proyecto, utiliza el siguiente comando:

python flask_crud_orm/app/__init__.py
(ten en cuenta el path completo y tu ubicacion relativa), puede ser ejecutado de la forma que le sea conveniente, siendo apropiado para un archivo py.

Una vez que el proyecto esté en ejecución, abre tu navegador y accede a la aplicación en http://localhost:5000. Si se configuro con los valores de host y puerto por defecto.