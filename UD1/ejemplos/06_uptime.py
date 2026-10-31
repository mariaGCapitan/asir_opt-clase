# 06_uptime.py — Convertir segundos de uptime en días, horas, minutos y segundos.
# Linux guarda el tiempo que lleva encendido el equipo, en segundos, en /proc/uptime.

uptime = int(input("Segundos encendido: "))

dias = uptime // 86400          # un día tiene 86400 segundos
resto = uptime % 86400

horas = resto // 3600           # una hora tiene 3600 segundos
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

print(f"El servidor lleva {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos encendido")
