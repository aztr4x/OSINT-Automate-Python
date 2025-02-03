# OSINT-Automate-Python
Estos son un conjunto de scripts que tienen como objetivo automatizar el monitoreo de telegram combinando el uso de OSINT &amp; Threat intelligence

# Funcionalida de los scrtips
- script1.py = Este script se encarga de extraer la información de un usuario en telegram de forma automatizada usando @usuario
- script2.py = Este script se encarga de extraer todos los mensajes de un grupo de telegram y monitorearlo
- script3.py = Este script es como el "script2.py" pero se integraron expresiones regulares para filtrar contenido y usarlo para un enfoque de Threat intelligence
- scriptalternativo.py = Este script lo tuve que crear para extraer los links y ids de los grupos a los que pertenecezo para integrarlo con los demás scripts

# Paso 1
Se tiene que tener principalmente una cuenta de telegram activa y funcionando para poder solicitar una API_ID y HASH_ID.

1) Ingresar en https://my.telegram.org/auth
2) Autenticarse con su número de telefono para obtener los IDS
3) Obtener HASH_ID API_ID (No compartirlos con nadie)

# Paso 2
1) Se debe personalizar los scripts manualmente cambiando las variales
   HASH_ID = "VA TU ID DE HASH"
   API_ID = "VA TU API ID"
   NUMERO TEL= "DEBES COLOCAR TU NUMERO DE TELEFONO" (El formato debe ser con código de país internacional por ejemplo para México es +52)

2) Darle permisos al script chmod +x en linux

# Paso 3
1) Es importante instalar la librería telethon puedes usar
- python3 -m pip install --upgrade pip
- python3 -m pip install --upgrade telethon
