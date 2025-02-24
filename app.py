
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Generar clave de inicialización
clave = get_random_bytes(16)
cipher = AES.new(clave, AES.MODE_EAX)

# Solicitar el texto a cifrar
texto = input("\nTexto a Cifrar: ")

# Crear directorio si no existe
if not os.path.exists("archivos"):
    os.makedirs("archivos")

# Cifrar texto
mensaje = texto.encode()
print("")
print("Texto a Cifrar:", texto)
print("")

cifrado, tag = cipher.encrypt_and_digest(mensaje)
print("Texto Cifrado:", cifrado)
print("")
# Guardar el Texto cifrado en un archivo
with open("archivos/cifrado.txt", "wb") as file:
    file.write(cifrado)

# Descifrar Texto
cipher_dec = AES.new(clave, AES.MODE_EAX, cipher.nonce)
mensaje_descifrado = cipher_dec.decrypt(cifrado).decode()
print("Mensaje Descifrado:", mensaje_descifrado)
print("")
# Guardar el Texto descifrado en un archivo
with open("archivos/descifrado.txt", "w") as file:
    file.write(mensaje_descifrado)
