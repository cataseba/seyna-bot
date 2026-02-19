import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
SELLER_ID = int(os.environ.get("SELLER_ID"))


def obtener_publicaciones_activas():
    url = f"https://api.mercadolibre.com/users/{SELLER_ID}/items/search?status=active"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if "results" not in data:
        print("Error obteniendo publicaciones:", data)
        return []

    return data["results"]


def obtener_detalle_item(item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return response.json()