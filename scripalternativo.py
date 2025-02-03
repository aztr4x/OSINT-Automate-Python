from telethon.sync import TelegramClient

# Configuración: Reemplaza con tus credenciales
API_ID = "ID_API"
API_HASH = "ID_HASH"
PHONE_NUMBER = "NUMERO_TELEFONO"

# Iniciar sesión
client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

async def obtener_grupos():
    """Obtiene y muestra los IDs de los grupos en los que estás agregado."""
    await client.start()
    dialogs = await client.get_dialogs()

    print("🔍 Tus grupos en Telegram:")
    for chat in dialogs:
        if chat.is_group:
            print(f"Grupo: {chat.title} | ID: {chat.id}")

    await client.disconnect()

if __name__ == "__main__":
    import asyncio
    asyncio.run(obtener_grupos())
