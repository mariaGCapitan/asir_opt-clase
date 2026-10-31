# 04_cadenas_fstrings.py — Juntar texto y números para mostrar mensajes.

servidor = "srv-web-01"
ip = "192.168.1.10"
usado = 375
total = 500

# Concatenar con + solo funciona entre cadenas
print("Servidor: " + servidor)
# print("Usado: " + usado)    # TypeError: no se puede sumar str + int

# La forma moderna: f-strings. Lo que va entre llaves se calcula.
print(f"Servidor {servidor} con IP {ip}")
print(f"Disco: {usado} de {total} GB")
print(f"Ocupado: {usado / total * 100} %")

# Formato dentro de las llaves
porcentaje = usado / total * 100
print(f"Ocupado: {porcentaje:.1f} %")         # 1 decimal
print(f"Ocupado: {porcentaje:.0f} %")         # sin decimales
print(f"Bytes: {total * 1024 ** 3:,}")        # separador de miles
print(f"[{servidor:<15}] [{usado:>6}]")       # alineado a la izquierda / derecha

# Caracteres especiales
print("Línea 1\nLínea 2")            # \n → salto de línea
print("Nombre:\tsrv-web-01")         # \t → tabulador
print("Ruta: C:\\Users\\admin")      # \\ → una barra invertida
print(r"Ruta: C:\Users\admin")       # r"" → cadena "cruda": las barras se quedan como están

# Algunas operaciones con cadenas
print(len(servidor))                       # longitud
print(servidor.upper())                    # a mayúsculas
print("  texto con espacios  ".strip())    # quita espacios de los extremos
print("=" * 40)                            # repetir una cadena
