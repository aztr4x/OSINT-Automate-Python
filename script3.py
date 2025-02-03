from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio
import re

# Configuración: Reemplaza con tus credenciales
API_ID = "ID_API"
API_HASH = "ID_HASH"
PHONE_NUMBER = "NUMERO_TELEFONO"
GRUPOS_A_MONITOREAR = ["LINK DE TU GRUPO A MONITOREAR"]  # Links de los grupos a monitorear

# Expresiones regulares para detectar términos clave
PATRONES = [
    r"\bacademia[- ]?de[- ]?ciberseguridad\b",  # Detecta "Academia de Ciberseguridad" con o sin espacios o guiones
    r"academia-ciberseguridad\.com",  # Detecta el dominio exacto
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # Detecta correos electrónicos
]

# Iniciar sesión
client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

async def join_groups():
    """Se une automáticamente a los grupos especificados."""
    await client.start()
    for group in GRUPOS_A_MONITOREAR:
        try:
            await client(JoinChannelRequest(group))
            print(f"✅ Unido a {group}")
        except Exception as e:
            print(f"⚠️ No se pudo unir a {group}: {e}")

@client.on(events.NewMessage)
async def monitorear_mensajes(event):
    """Monitorea los mensajes en los grupos y filtra según expresiones regulares."""
    sender = await event.get_sender()
    mensaje = event.raw_text.lower()
    
    print(f"📩 Mensaje recibido en: {event.chat.title} (ID: {event.chat.id}) -> {mensaje}")
    
    # Verifica si el mensaje contiene alguna coincidencia con los patrones
    for patron in PATRONES:
        if re.search(patron, mensaje, re.IGNORECASE):
            print(f"🔍 Coincidencia detectada en {event.chat.title}: {mensaje}")
            with open("monitoreo_keywords.txt", "a", encoding="utf-8") as file:
                file.write(f"[{event.date}] {event.chat.title}: {mensaje}\n")
            break  # Detener la búsqueda una vez que encuentra una coincidencia

async def main():
    await join_groups()
    print("🔍 Monitoreando palabras clave en los grupos...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
