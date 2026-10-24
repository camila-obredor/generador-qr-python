"""Programa principal del generador de códigos QR"""

from generador_qr import generar_qr


def pedir_contenido() -> str:
    """Solicita al usuario el contenido que tendrá el código QR"""
    return input("Ingresá el texto o URL para generar el QR: ").strip()


def pedir_nombre_archivo() -> str:
    """Solicita al usuario el nombre del archivo de imagen"""
    return input("Ingresá un nombre para el archivo: ").strip()


def main() -> None:
    """Ejecuta el programa principal del generador de códigos QR"""

    print("==============================")
    print("   GENERADOR DE CÓDIGOS QR")
    print("==============================")

    try:
        contenido = pedir_contenido()
        nombre_archivo = pedir_nombre_archivo()

        ruta_archivo = generar_qr(contenido, nombre_archivo)

        print()
        print("¡Código QR generado correctamente!")
        print("Archivo guardado en:", ruta_archivo)

    except ValueError as error:
        print("Error:", error)

    except OSError as error:
        print("No se pudo guardar la imagen.")
        print("Detalle del error:", error)


if __name__ == "__main__":
    main()


# End of program