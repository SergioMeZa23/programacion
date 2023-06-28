Algoritmo ejercicio1
	definir costo, uso, gasto como real
	definir lugar como caracter 
	escribir "contratacion de amazon web"
	escribir ""
	escribir "elija lugar del servidor"
	escribir ""
	escribir "1 Norteamérica 0,02 USD por GB usado"
	escribir "2 Centroamérica 0,03 USD por GB usado"
	escribir "3 Sudamérica 0,05 USD por GB usado"
	Escribir "4 Europa 0,07 USD por GB usado"
	escribir "5 Asia/Oceanía 0,09 USD por GB usado"
	escribir "(1|2|3|4|5)"
	leer lugar 
	
	norteamerica=0.02
	centroamerica=0.03
	sudamerica=0.05
	europa=0.07
	asia=0.09
	
	escribir "indique uso de GB"
	leer uso
	
	Segun uso Hacer
		opcion_1:
			escribir "el costo seleccionado de norteamerica es," gasto=uso*0.02
			escribir "el costo seleccionado de centroamerica es," gasto=uso*0.03
			escribir "el costo seleccionado de sudamerica es," gasto=uso*0.05
			escribir "el costo seleccionado de europa es," gasto=uso*0.07
			escribir "el costo seleccionado de asia/oceania es," gasto=uso*0.09
			
			
			
		
			
			
			
			
			
	
	Fin Segun
	
	

FinAlgoritmo
