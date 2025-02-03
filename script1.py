from telethon.sync import TelegramClient
import os

# Configuración: Reemplaza con tus credenciales
API_ID = "ID_API"
API_HASH = "ID_HASH"
PHONE_NUMBER = "NUMERO_TELEFONO"

# Iniciar sesión
client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)

async def obtener_info_usuario(username):
    """Obtiene la información completa de un usuario de Telegram y la guarda en un archivo txt."""
    await client.start()
    try:
        user = await client.get_entity(username)
        filename = f"{username}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"ID: {user.id}\n")
            file.write(f"Nombre: {user.first_name}\n")
            file.write(f"Apellido: {user.last_name if user.last_name else 'No disponible'}\n")
            file.write(f"Username: {user.username if user.username else 'No disponible'}\n")
            file.write(f"Número de Teléfono: {user.phone if user.phone else 'No disponible'}\n")
            file.write(f"Bio: {user.about if hasattr(user, 'about') else 'No disponible'}\n")
        
        # Descargar foto de perfil si existe
        if user.photo:
            profile_photo_path = await client.download_profile_photo(user, file=f"{username}_photo.jpg")
            file.write(f"Foto de perfil guardada en: {profile_photo_path}\n")
        
        print(f"Información guardada en {filename}")
    except Exception as e:
        print(f"Error obteniendo datos: {e}")
    await client.disconnect()

if __name__ == "__main__":
    username = input("Ingresa el username de Telegram (@usuario): ")
    import asyncio
    asyncio.run(obtener_info_usuario(username))