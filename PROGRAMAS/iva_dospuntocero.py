precio_bruto = float (input ("Ingrese el precio bruto: "))
IVA = float(input("Ingrese el porcentaje del IVA: "))
IVA = 1 + IVA / 100
precio_final = precio_bruto * IVA
print ( "El precio final es: ",round(precio_final,2))