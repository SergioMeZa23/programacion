Algoritmo ejercicio
	definir n1, n2, n3, perimetro, area, s Como Real
	escribir "ingrese los valores de los lados"
	leer n1,n2,n3
	
	perimetro=n1+n2+n3
	escribir "el perimetro es," perimetro
	s= perimetro / 2
	area= rc(s*(s-n1)*(s-n2)*(s-n3))
	escribir "el area es," area
	
	si (n1=n2 y n1=n3) Entonces
		escribir "el trinagulo es equilatero"
		sino
		
		si (n1=n2 o n1=n3) Entonces
			escribir "el triangulo es isosceles"
			
		SiNo
			escribir "el triangulo es escaleno"
			
		
		
	 
		
	FinSi
	
     fin si 
     
	
	
FinAlgoritmo
