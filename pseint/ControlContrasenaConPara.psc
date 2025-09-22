Algoritmo ControlContrasenaConPara
	Definir contrasenaCorrecta, entrada Como Cadena
	Definir intento Como Entero
	Definir exito, NOexito Como Logico
	
	contrasenaCorrecta <- "123"
	exito <- Falso
	NOexito <- Verdadero // usar <-
	
	Para intento <- 1 Hasta 3 Hacer
		// Solo pedir si aún no se logró el acceso
		Si NOexito Entonces
			Escribir "Intento ", intento, " de 3. Ingrese la contraseña:"
			Leer entrada
			
			Si entrada = contrasenaCorrecta Entonces
				Escribir "Acceso concedido."
				exito <- Verdadero
				NOexito <- Falso // corta futuras preguntas dentro del PARA
			SiNo
				Si intento < 3 Entonces
					Escribir "Contraseña incorrecta. Intente nuevamente."
				FinSi
			FinSi
		FinSi
	FinPara
FinAlgoritmo