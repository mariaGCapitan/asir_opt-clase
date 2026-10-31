# 02_variables_tipos.py — Guardar datos en variables y ver de qué tipo son.

nombre_servidor = "srv-web-01"     # str   → cadena de texto
num_cpus = 4                       # int   → número entero
carga_media = 0.75                 # float → número con decimales
en_produccion = True               # bool  → verdadero o falso

print(nombre_servidor)
print(num_cpus)
print(carga_media)
print(en_produccion)

# type() dice de qué tipo es un valor
print(type(nombre_servidor))
print(type(num_cpus))
print(type(carga_media))
print(type(en_produccion))

# Una variable puede cambiar de valor
num_cpus = 8
print(num_cpus)
