# Reto 5 — De días, horas, minutos y segundos a segundos (el camino inverso al ejemplo del uptime).

dias = int(input("Días: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos

print(f"Son {total_segundos:,} segundos")
