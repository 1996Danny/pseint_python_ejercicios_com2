Algoritmo bucles_mientras
	// necesitamos un algoritmo que controle el ingreso de contraseña (3 veces max)
	Definir contrasenia, ingreso_cont Como Entero
	contrasenia = 1234
	
	contador = 0
	
	Mientras contrasenia <> ingreso_cont Y contador <> 3 Hacer
		
		Imprimir "Ingrese su contraseña"
		Leer ingreso_cont
		
		imprimir "Contraseña incorrecta"
		contador = contador + 1 
		
	FinMientras
	
	
	
FinAlgoritmo
