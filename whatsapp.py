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
    desc = item.get("description", {}).get("plain_text", "")
    desc_corta = (desc[:200] + "...") if len(desc) > 200 else desc

    # Emoji y formato profesional
    mensaje = f"🔥 *{titulo}* 🔥\n\n"
    mensaje += f"{desc_corta}\n\n"
    mensaje += f"💲 *Precio:* ${precio}\n"
    mensaje += f"📦 Envíos a todo el país\n"
    mensaje += f"👉 Ver en Mercado Libre: {link}\n\n"
    mensaje += f"📍 Colectora Panamericana Oeste, Ramal Escobar 3250 – Ing. Maschwitz\n"
    mensaje += f"🕒 Lun a Vie 9-18 hs | Sáb 9:30-13 hs\n"
    mensaje += f"✅ Consultanos y aprovechá las promos de hoy 👇\n"
    mensaje += f"https://wa.me/1123411103"

    return mensaje
