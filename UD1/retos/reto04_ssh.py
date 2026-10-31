
# Reto 4 — Generador de comandos de conexión.
# Pedir usuario, servidor y puerto, y construir los comandos ssh y scp listos para copiar.

usuario = input("Usuario: ")
host = input("Servidor (nombre o IP): ")
puerto = input("Puerto SSH: ")

print()
print("Conectar al servidor:")
print(f"  ssh -p {puerto} {usuario}@{host}")
print()
print("Copiar un archivo al servidor:")
print(f"  scp -P {puerto} archivo.txt {usuario}@{host}:/home/{usuario}/")
