# Generador de Códigos QR

El proyectpo permite generar códigos QR a partir de un texto o una URL ingresada por el usuario.

El programa solicita el contenido que se desea guardar dentro del código QR y un nombre para el archivo. Luego genera una imagen en formato PNG y la guarda dentro de la carpeta `qr_generados`.

## Funcionalidades

- Ingresar un texto o una URL.
- Generar un código QR con ese contenido.
- Elegir el nombre del archivo.
- Guardar automáticamente el QR como imagen PNG.
- Validar que los datos ingresados no estén vacíos.
- Manejar errores mediante `try / except`.


## Instalación

Primero se debe clonar el repositorio:

```bash
git clone https://github.com/camila-obredor/generador-qr-python.git
```

Luego ingresar a la carpeta del proyecto:

```bash
cd generador_qr
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```

El programa solicitará el texto o URL que se desea convertir en código QR y el nombre del archivo.

Ejemplo:

```text
==============================
   GENERADOR DE CÓDIGOS QR
==============================

Ingresá el texto o URL para generar el QR: https://www.google.com
Ingresá un nombre para el archivo: google

¡Código QR generado correctamente!
Archivo guardado en: qr_generados\google.png
```

## Integrantes
- Camila Obredor
