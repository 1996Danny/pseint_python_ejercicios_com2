Algoritmo control_contrase�a_para
	Definir contrasenia, ingreso_cont Como Entero
	Definir i Como Entero
	Definir correcto Como Logico
	
	contrasenia = 1234
	correcto = FALSO
	
	Para i Desde 1 Hasta 3
		Si correcto == FALSO Entonces
			Imprimir "Ingrese su contrase�a:"
			Leer ingreso_cont
			
			Si ingreso_cont == contrasenia Entonces
				Imprimir "Contrase�a correcta"
				correcto = VERDADERO
			SiNo
				Imprimir "Contrase�a incorrecta"
			FinSi
		FinSi
	FinPara
	
	Si correcto == FALSO Entonces
		Imprimir "Demasiados intentos. Acceso denegado."
	FinSi
FinAlgoritmo