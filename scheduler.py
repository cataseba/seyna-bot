import time
from mercadolibre import obtener_publicaciones_activas, obtener_detalle_item
from whatsapp import generar_mensaje

# Configuración
TIEMPO_ENTRE_PUBLICACIONES = 3600  # 1 hora en segundos
PUBLICACIONES_POR_DIA = 40

# Lista para controlar qué productos ya se publicaron
productos_publicados = []

def main():
    print("🟢 Bot Seyna iniciado...")
    contador_dia = 0

    while contador_dia < PUBLICACIONES_POR_DIA:
        print(f"🔄 Iteración: {contador_dia + 1}")

        publicaciones = obtener_publicaciones_activas()

        for item_id in publicaciones:
            if item_id in productos_publicados:
                continue

            detalle = obtener_detalle_item(item_id)
            mensaje = generar_mensaje(detalle)

            # Aquí iría la integración con WhatsApp (Web o API)
            # Por ahora solo imprimimos para test
            print("\n====================")
            print(mensaje)
            print("====================\n")

            productos_publicados.append(item_id)
            contador_dia += 1

            if contador_dia >= PUBLICACIONES_POR_DIA:
                break

            print(f"⏱ Esperando {TIEMPO_ENTRE_PUBLICACIONES} segundos hasta la siguiente publicación...")
            time.sleep(TIEMPO_ENTRE_PUBLICACIONES)

    print("✅ Se completaron las publicaciones del día.")

if __name__ == "__main__":
    main()
