# Repositorio con ejercicios de programación orientada a objetos en Python.

## 1. Crear el archivo .gitignore

Configurar el archivo .gitignore para restringir los archivos a sincronizar.

````shell
*.pyc
_pycache_/
````

## 2. Indexar archivos y carpetas

Permite indexar todos los archivos y carpetas del proyecto, para identificar los cambios.

````shell
git add .
````

## 3. Crear un punto de control (COMMIT)

Creamos un punto de control con  los cambios realizados en el proyecto. Es como una copia para poder ver los cambios de un proyecto. El nombre del archivo funciona con un verbo, en este caso (CREATED).

````shell
git commit -m "CREATED. gitignore"
````

* CREATED - Crear nuevos archivos o directorios.
* UPDATE - Actualizar módulos del sistema.
* FIXED - Corregir errores del sistema.

## 4. Sincronizar los cambios con el repositorio

Sincronizar los cambios entre el repositorio (la rama principal).

````shell
git push -u origin main
````


