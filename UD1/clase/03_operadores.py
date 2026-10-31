# Operaciones con números. Ejemplo: el disco de un servidor

total_gb = 500
usado_gb = 375

libre_gb = total_gb - usado_gb
porcentaje_usado = usado_gb / total_gb * 100

print("Total de disco:",total_gb, "GB")

print("Total disco:"+str(total_gb)+"GB") # convirtiendo el número a texto

print("Disco usado:",usado_gb, "GB")
print("Libre:", libre_gb, "GB")
print("Ocupado:",porcentaje_usado, "%")

# podemos redondear un número
prueba = 5/3
print(round(prueba,2))

#Comparaciones

print(usado_gb == total_gb)
print(porcentaje_usado>=70)

IVA = 20
print('Esto es que nos dice  la teoría')