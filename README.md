# aplicacion-criaturas-python-gtk-mysql
Programación Avanzada en Python: Aplicación gráfica para gestionar la información de criaturas en una base de datos usando **Python**, **Mysql** y **GTK+**

# Requisitos
* **Python 3**
* Librerías **GTK+ 3** y **PyGObject**

# Base de datos

Para ejecutar la aplicación correctamente es necesario tener configurado un servidor de base de datos, preferiblemente "MySQL Server", con las siguientes características:

* **Nombre del servidor:** 'localhost'
* **Nombre de la base de datos:** 'Criaturas'
* **Nombre de usuario de la base de datos:** 'usuario'
* **Contraseña para el usuario de la base da datos:** 'contra'
* **Nombre de la tabla:** 'Criatura'

Si no tiene acceso a un servidor de bases de datos con esta configuración, puede realizar uno de los siguientes pasos:

1.  **Ejecutar** el fichero **"configurar_bd.sql"** a través de una consola de comandos disponible en su 
    servidor de bases de datos. Este fichero consta de varias sentencias de tipo "SQL" que realizan lo 
    siguiente:
    * Creación de la base de datos "Criaturas"
    * Creación del usuario "usuario" con contraseña "contra" con y acceso a la base de datos "Criaturas"
    * Creacion de la tabla "Criatura", perteneciente a la base de datos "Criaturas"
    * Insercion de una tupla en la tabla "Criatura"

    Ejemplo: En un sistema operativo perteneciente a la familia GNU/Linux, con la consola de comandos "bash" y "MySQL Server", puede ejecutarse la siquiente instrucción:

    `$ > mysql --user="<usuario>" --password="<password>" < "<directorio_fichero_sql>/configurar_bd.sql"`

    O, si ya se ha iniciado la sesión en la consola de comandos del sistema gestor de bases de datos:

    `mysql> source "<directorio_fichero_sql>/configurar_bd.sql";`

2.  **Editar** la configuración de **conexión a la base de datos**, de manera que pueda usar su propia 
    base de datos, usuario, table, etc... Para realizar esto puede modificar los valores asociados a las 
    variables que se encuentran entre las líneas 7 y 10 del fichero **"criaturas.py"**.