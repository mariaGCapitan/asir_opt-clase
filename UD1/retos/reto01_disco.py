# Reto 1 — Ocupación de disco.
# Con los datos en variables, mostrar GB libres y porcentajes de ocupado y libre, con 1 decimal.

total_gb = 2000
usado_gb = 1450

libre_gb = total_gb - usado_gb
porcentaje_usado = usado_gb / total_gb * 100
porcentaje_libre = 100 - porcentaje_usado

print("Libre:", libre_gb, "GB")
print("Ocupado:", round(porcentaje_usado, 1), "%")
print("Libre:", round(porcentaje_libre, 1), "%")
