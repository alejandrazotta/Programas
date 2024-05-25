cotizacion = float (input ("Ingrese el cotizacion del dia: "))
print( "Ingrese el monto a convertir en la moneda correspondentiente ")
pesos = input("Ingrese el monto en pesos: ")
if pesos == "":
    pesos = 0
else:
    pesos = float(pesos)
usd = input("Ingrese el monto en USD: ")
if usd == "":
    usd = 0
else:
    usd = float(usd)
if pesos == 0:
    valor = usd * cotizacion
    print ( usd, " USD son ", round(valor,2), "pesos")
else:
    valor = pesos / cotizacion
    print( pesos, " pesos son ", round(valor,2), "USD")
