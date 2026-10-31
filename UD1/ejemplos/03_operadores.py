# 03_operadores.py — Operaciones con números: el disco de un servidor.

total_gb = 500
usado_gb = 375

libre_gb = total_gb - usado_gb
porcentaje_usado = usado_gb / total_gb * 100

print("Total:", total_gb, "GB")
print("Usado:", usado_gb, "GB")
print("Libre:", libre_gb, "GB")
print("Ocupado:", porcentaje_usado, "%")

# División normal (siempre da float), división entera y resto
print(7 / 2)     # 3.5
print(7 // 2)    # 3
print(7 % 2)     # 1
print(2 ** 10)   # 1024 → potencia: 2 elevado a 10

# round() redondea a los decimales que se le pidan
print(round(porcentaje_usado, 1))

# Comparaciones: el resultado es un bool
print(usado_gb > total_gb)       # False
print(porcentaje_usado >= 70)    # True
print(libre_gb == 125)           # True → dos iguales para COMPARAR
