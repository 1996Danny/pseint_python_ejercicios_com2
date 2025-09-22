Algoritmo bucles_para
	// necesitamos un algoritmo que controle el ingreso de contraseña (3 veces max)
	Definir contrasenia, ingreso_cont Como Entero
	contrasenia = 1234

	
	Para i Desde 1 Hasta 3 Hacer
		Imprimir "Ingrese su contraseña"
		Leer ingreso_cont
		si contrasenia == ingreso_cont Entonces
			Imprimir "Contraseña correcta"
			i=5
		FinSi
		
		Si contrasenia <> ingreso_cont Entonces
			Imprimir "Contraseña incorrecta"
		FinSi
		
	FinPara
FinAlgoritmo
