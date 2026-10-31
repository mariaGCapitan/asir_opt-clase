#!/usr/bin/env python3
"""
Las actualizaciones solo se aplican entre las 2:00 y las 5:00 de un día laborable.
"""

# --- Datos de entrada ---
hora = int(input("Hora actual (0-23): "))
dia = input("Día de la semana: ").lower() #Convertimos el día de la semana que el usuario introduce a minúsculas

# --- Condiciones ---

#Vamos a comprobar si es fin de semana o no
if dia == "sábado" or dia == "domingo":
    es_fin_de_semana = True
else:
    es_fin_de_semana = False


#Vamos a comprobar si podemos actualizar
if hora >= 2 and hora < 5 and es_fin_de_semana == False:
    print("Se pueden aplicar actualizaciones")
else:
    print("Estás fuera del horario o día de actualizaciones")