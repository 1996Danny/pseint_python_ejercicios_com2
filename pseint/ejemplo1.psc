Algoritmo control_contrase�a_mientras
	Definir contrasenia, ingreso_cont, intentos Como Entero
	contrasenia = 1234
	intentos = 0
	
	Mientras intentos < 3
		Imprimir "Ingrese su contrase�a:"
		Leer ingreso_cont
		intentos = intentos + 1
		
		Si ingreso_cont == contrasenia Entonces
			Imprimir "Contrase�a correcta"
			intentos = 3
		SiNo
			Imprimir "Contrase�a incorrecta"
		FinSi
	FinMientras
	
	Si ingreso_cont <> contrasenia Entonces
		Imprimir "Demasiados intentos. Acceso denegado."
	FinSi
FinAlgoritmo