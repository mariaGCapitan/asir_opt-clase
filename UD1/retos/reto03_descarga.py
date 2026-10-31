# Reto 3 — Tiempo de descarga.
# Tamaño en MB y velocidad en Mbps (megabits por segundo). Un byte son 8 bits.

tamano_mb = float(input("Tamaño del archivo en MB: "))
velocidad_mbps = float(input("Velocidad de la conexión en Mbps: "))

segundos_total = int(tamano_mb * 8 / velocidad_mbps)
minutos = segundos_total // 60
segundos = segundos_total % 60

print(f"La descarga tardará unos {minutos} minutos y {segundos} segundos")
