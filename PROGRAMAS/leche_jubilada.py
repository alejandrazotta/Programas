jubilado_nro = int (input ("ingrese 0 si es jubilado 1 si no lo es: "))
cantidad = int (input ("Cantidad de leche: "))
if jubilado_nro == 0:
    descuento = 0.10
if cantidad > 12 and cantidad <= 24:
    descuento = descuento + 0.10
if cantidad > 24:
    descuento = descuento + 0.15
importe_total = cantidad * 1000 * (1-descuento)
print ("Importe Total: ", importe_total, " Descuento aplicado: ", descuento * 100, "%")