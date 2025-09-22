Algoritmo control_contraseña_mientras
	Definir contrasenia, ingreso_cont, intentos Como Entero
	contrasenia = 1234
	intentos = 0
	
	Mientras intentos < 3
		Imprimir "Ingrese su contraseña:"
		Leer ingreso_cont
		intentos = intentos + 1
		
		Si ingreso_cont == contrasenia Entonces
			Imprimir "Contraseña correcta"
			intentos = 3
		SiNo
			Imprimir "Contraseña incorrecta"
		FinSi
	FinMientras
	
	Si ingreso_cont <> contrasenia Entonces
		Imprimir "Demasiados intentos. Acceso denegado."
	FinSi
FinAlgoritmo