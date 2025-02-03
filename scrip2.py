from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio

# Configuración: Reemplaza con tus credenciales
API_ID = "ID_API"
API_HASH = "ID_HASH"
PHONE_NUMBER = "NUMERO_TELEFONO"
MONITOREADO = "@usuario_a_monitorear"  # Username del usuario a monitorear
GRUPOS_A_MONITOREAR = ["link de tu grupo a monitorear"]  # Links de los grupos a monitorear

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
async def monitorear_usuario_en_grupo(event):
    """Monitorea todos los mensajes en los grupos especificados y detecta actividad del usuario monitoreado."""
    sender = await event.get_sender()
    print(f"📩 Mensaje recibido en: {event.chat.title} (ID: {event.chat.id}) -> {event.raw_text}")
    
    if sender.username and sender.username.lower() == MONITOREADO.lower():
        print(f"🔔 {sender.first_name} ha publicado en {event.chat.title}: {event.raw_text}")
        with open("monitoreo_usuario.txt", "a", encoding="utf-8") as file:
            file.write(f"[{event.date}] {sender.first_name} en {event.chat.title}: {event.raw_text}\n")

async def get_recent_messages():
    """Obtiene los últimos mensajes de los grupos monitoreados."""
    for group in GRUPOS_A_MONITOREAR:
        async for message in client.iter_messages(group, limit=5):
            print(f"📜 {message.date} | {message.sender_id}: {message.text}")

async def main():
    await join_groups()
    await get_recent_messages()
    print("🔍 Monitoreando la actividad en los grupos...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
