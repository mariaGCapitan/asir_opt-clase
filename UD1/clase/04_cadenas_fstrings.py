# Unir texto y números en un mensaje
servidor = "srv-web_01"
ip="192.168.1.10"
usado=375
total=500

#print("Servidor: " + servidor)
#print("Usado: " + usado) #error porque no es un str

#Usando f-strings

#print(f"Servidor {servidor} con IP {ip}")
#print(f"Disco: {usado} GB de {total} GB")
#print(f"Ocupado: {usado /total * 100} %") #Lo que está entre llaves se calcula

#Formato dentro de las llaves
porcentaje = usado / total * 100
print(f"Ocupado: {porcentaje:.1f} %") #1 decimal
print(f"Ocupado: {porcentaje:.0f} %") # son decimales
print(f"Bytes: {total * 1024 ** 3:,}") #Separador de miles
print(f"[{servidor:<15}][{usado:>6}]") #Alineado a la izquierda y a la derecha


#Caracteres especiales
print("Línea 1\nLínea 2") #\n un salto de línea
print("Nombre:\tsrv-web-01")
print("Ruta: C:\\Users\\admin")
print(r"Ruta: C:\Users\admin")

#Operaciones con cadenas
print(len(servidor)) #Longitud
print(servidor.upper())
cadena="   texto con espacios  "
print(cadena.strip()) #Quita los espacios de los extremos
print("=" * 40)
print("MENÚ DE CONFIGURACIÓN SERVIDOR")
print("=" * 40)
