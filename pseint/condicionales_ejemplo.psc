Algoritmo condicionales_ejemplo
	// necesitamos saber si una persona puede votar(16 años)
	Definir edad Como Entero
	
	Imprimir "Ingrese su edad: "
	Leer edad
	
	// edad >= 16
	Si edad > 15 Entonces
		Imprimir "Usted está habilitado para votar!!"
	SiNo
		Imprimir "la condición fue FALSA, no puede votar"
	FinSi
	
	
FinAlgoritmo
