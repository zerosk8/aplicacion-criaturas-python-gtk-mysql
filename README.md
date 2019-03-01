# aplicacion-criaturas-python-gtk-mysql
Programación Avanzada en Python: Aplicación gráfica para gestionar la información de criaturas en una base de datos usando **Python**, **Mysql** y **GTK+**

# 1. Requisitos
* **Python 3**
* Librerías **GTK+ 3** y **PyGObject**

## 1.2 Base de datos

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

    Si ya se ha iniciado la sesión en la consola de comandos del sistema gestor de bases de datos:

    `mysql> source "<directorio_fichero_sql>/configurar_bd.sql";`

2.  **Editar** la configuración de **conexión a la base de datos**, de manera que pueda usar su propia 
    base de datos, usuario, table, etc... Para realizar esto puede modificar los valores asociados a las 
    variables que se encuentran entre las líneas 7 y 10 del fichero **"criaturas.py"**.

# 2. Capturas de pantalla

![GUI obtención de criatura](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_obtencion_criatura.png)

![GUI obtención de criatura, mensaje de advertencia](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_obtencion_criatura_mensaje_advertencia.png)

![GUI creacion de criatura](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_creacion_criatura.png)

![GUI creacion de criatura, mensaje de advertencia](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_creacion_criatura_mensaje_advertencia.png)

![GUI creacion de criatura, mensaje de éxito](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_creacion_criatura_mensaje_exito.png)

![GUI actualización de criatura](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_actualizacion_criatura.png)

![GUI actualización de criatura, mensaje de advertencia](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_actualizacion_criatura_mensaje_advertencia.png)

![GUI actualización de criatura, mensaje de éxito](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_actualizacion_criatura_mensaje_exito.png)

![GUI eliminación de criatura](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_eliminacion_criatura.png)

![GUI eliminación de criatura, mensaje de advertencia](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_eliminacion_criatura_mensaje_advertencia.png)

![GUI eliminación de criatura, mensaje de éxito](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_eliminacion_criatura_mensaje_exito.png)

![GUI acerca de](https://github.com/zerosk8/aplicacion-criaturas-python-gtk-mysql/blob/master/documentacion/imagenes/gui_acerca_de.png)