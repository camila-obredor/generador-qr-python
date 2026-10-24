"""Funciones para generar códigos QR"""

from pathlib import Path

import qrcode
from PIL import Image


def generar_qr(contenido: str, nombre_archivo: str) -> Path:
    """Genera un código QR y lo guarda como una imagen PNG."""

    if contenido.strip() == "":
        raise ValueError("El contenido del código QR no puede estar vacío.")

    if nombre_archivo.strip() == "":
        raise ValueError("El nombre del archivo no puede estar vacío.")

    if not nombre_archivo.lower().endswith(".png"):
        nombre_archivo = nombre_archivo + ".png"

    carpeta_salida = Path("qr_generados")
    carpeta_salida.mkdir(exist_ok=True)

    ruta_archivo = carpeta_salida / nombre_archivo

    codigo_qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )

    codigo_qr.add_data(contenido)
    codigo_qr.make(fit=True)

    imagen_qr = codigo_qr.make_image(
        fill_color="black",
        back_color="white",
    )

    imagen_qr.save(ruta_archivo)

    with Image.open(ruta_archivo) as imagen:
        imagen.verify()

    return ruta_archivo