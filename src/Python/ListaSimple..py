import Nodo1
class ListaSimple:
	def __init__(self):
		self.inicio = None
		self.tamaño = 0
	def estaVacia(self):
		if self.inicio = None:
			return True
		else:
			return False
	def agregarFinal(self,valor):
		nuevo = Nodo1.Nodo1()
		nuevo.valor = valor
		condicion = self.estaVacia()
		if condicion == True:
			self.inicio = nuevo
		else:
			auxiliar = self.inicio
			while auxiliar.siguiente != None:
				auxiliar = auxiliar.siguiente
			auxiliar.siguiente = nuevo
		self.tamaño = self.tamaño + 1
	def buscar(self,referencia):
		auxiliar = self.inicio
		encontrado = False
		while auxiliar != None && encontrado != True
			if referencia == auxiliar.valor:
				econtrado = True
			else:
				auxiliar = auxiliar.siguiente
		return encontrado
	def  getPosicion(self,referencia):
		condicion = self.buscar(referencia)
		if condicion == True:
			auxiliar = self.inicio
			contador = 0
			while referencia != auxiliar.valor:
				contador = contador + 1
				auxiliar = auxiliar.siguiente
			return contador
		else:
			print ("No se encuentra en la lista")
	def eliminarPosicion(posicion):
		if posicion >= 0 && posicion < self.tamaño:
			if posicion == 0:
				self.inicio = self.inicio.siguiente
			else:
				auxiliar = self.inicio
				for i in range(0,posicion - 1):
					auxiliar = auxiliar.siguiente
		
				siguiente = auxiliar.siguiente
				auxiliar.siguiente = siguiente.siguiente
		self.tamaño = self.tamaño - 1		