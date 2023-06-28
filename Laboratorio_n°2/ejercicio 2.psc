Algoritmo sin_titulo
	definir stock como real
	escribir "Stock Colun"
	escribir ""
	escribir "ingrese stock actual yogurt maqui"
	leer stock
	
	Mientras stock=1000 Hacer
		escribir "se llego a stock critico, solo quedan 1000 unidades"
		
	Fin Mientras
	
	Si stock=5000 entonces 
		escribir "precaucion, stock llego al 50%"
		
	SiNo
		si stock=3000 entonces
			escribir "stock llego al 30%"
		FinSi
	Fin Si
	
	si stock<=4999 entonces 
		escribir "stock bajo el 50%"
	FinSi
	
	si stock<=2999 entonces 
		escribir "stock bajo el 30%"
	FinSi
	
	si stock=0 Entonces
		escribir "reponer urgentemente"
	FinSi
	
	si stock>5000 entonces 
		escribir "stock adecuado"
	FinSi
	
	si stock<=999  entonces 
		escribir "stock ultra critico"
	FinSi

FinAlgoritmo
