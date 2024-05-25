Algoritmo leche_jubilada
	jubilado <- 0
	leche <- 0
	precio <- 1000
	importe_final <- 0
	Leer jubilado, unidades
	Si jubilado=0 Entonces
		descuento <- 0.10
	FinSi
	Si unidades>12 Y unidades<=24 Entonces
		descuento <- descuento+0.10
	FinSi
	Si unidades>24 Entonces
		descuento <- descuento+0.15
	FinSi
	importe_final <- unidades*precio*(1 - descuento)
	Escribir "$ ",importe_final, ' Descuento: ', descuento*100, '%'
FinAlgoritmo
