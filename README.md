# Examen Programación Web
PROGRAMACIÓN WEB/CONVALIDACION-26-FR

Aplicación web desarrollada con Python y Flask para la evaluación de la asignatura Programación Web.

## Descripción

El proyecto consiste en una aplicación web con un menú principal que permite acceder a dos ejercicios:

### Ejercicio 1: Compra de Pinturas

Permite ingresar:

- Nombre
- Edad
- Cantidad de tarros de pintura

Cada tarro tiene un valor de $9.000.

Descuentos aplicados:

| Rango de Edad | Descuento |
|--------------|------------|
| Menor de 18 años | 0% |
| Entre 18 y 30 años | 15% |
| Mayor de 30 años | 25% |

El sistema muestra:

- Nombre del comprador
- Total sin descuento
- Valor del descuento
- Total a pagar

### Ejercicio 2: Validación de Usuarios

El sistema considera dos usuarios registrados:

| Usuario | Contraseña | Rol |
|----------|------------|-----|
| juan | admin | Administrador |
| pepe | user | Usuario |

Resultados esperados:

- Bienvenido administrador juan
- Bienvenido usuario pepe
- Usuario o contraseña incorrectos

---

## Tecnologías Utilizadas

- Python3
- Flask
- HTML5
- CSS3
- Git
- GitHub

---

## Estructura del Proyecto

```text
ProyectoFlask/
│
├── main.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── ejercicio1.html
│   └── ejercicio2.html
│
└── README.md