from datetime import datetime

def generar_mensaje(item):
    """
    item: diccionario con info de Mercado Libre
    Debe contener:
      - title
      - price
      - permalink
      - description (opcional)
    """

    # Título
    titulo = item.get("title", "Producto sin título")

    # Precio
    precio = item.get("price", 0)

    # Link
    link = item.get("permalink", "")

    # Descripción acortada a 200 caracteres
    desc = item.get("description", {}).get("
