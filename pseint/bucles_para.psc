Algoritmo bucles_para
	// necesitamos un algoritmo que controle el ingreso de contrase�a (3 veces max)
	Definir contrasenia, ingreso_cont Como Entero
	contrasenia = 1234

	
	Para i Desde 1 Hasta 3 Hacer
		Imprimir "Ingrese su contrase�a"
		Leer ingreso_cont
		si contrasenia == ingreso_cont Entonces
			Imprimir "Contrase�a correcta"
			i=5
		FinSi
		
		Si contrasenia <> ingreso_cont Entonces
			Imprimir "Contrase�a incorrecta"
		FinSi
		
	FinPara
FinAlgoritmo
