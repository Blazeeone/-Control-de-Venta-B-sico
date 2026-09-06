# Sistema de Control de Venta Básico

Aplicación web desarrollada en Django para la digitalización y gestión de ventas de una pequeña tienda, implementando la arquitectura Modelo-Vista-Plantilla (MVT).

**Autor:** Yoshua Alberto Castillo Martínez  
**Carrera:** Analista Programador - INACAP Sede Renca  
**Asignatura:** Programación Back End (TI3041)  

## Funcionalidades Principales
* Registro de productos a vender con nombre, código, cantidad y precio.
* Actualización de stock y eliminación de productos.
* Visualización estructurada del listado de productos disponibles.
* Registro de ventas designadas a un RUT de cliente.
* Gestión de clientes con estructura de decisión: almacenamiento de datos para clientes habituales y registro de RUT exclusivo para clientes ocasionales (boleta).

## Tecnologías Utilizadas
* Backend: Python y Framework Django.
* Frontend: HTML/CSS mediante el motor de plantillas de Django.
* Base de datos: SQLite3 (entorno de desarrollo local).

## Instrucciones de Ejecución
1. Clonar este repositorio.
2. Crear y activar el entorno virtual (`python -m venv venv`).
3. Instalar las dependencias (`pip install django`).
4. Aplicar las migraciones de la base de datos (`python manage.py migrate`).
5. Levantar el servidor de desarrollo (`python manage.py runserver`).
