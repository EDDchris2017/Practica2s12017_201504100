import Nodo2
class ListaDoble:
	def __init__(self):
		self.inicio = None
	def insertar(self,valor):
		nuevo = Nodo2.Nodo2()
		nuevo.valor = valor
		if self.inicio == None:
			self.inicio = nuevo
		else:
			nuevo.siguiente = self.inicio
			self.inicio.anterior = nuevo
			self.inicio = nuevo
	def insertarFinal(self,valor):
		nuevo = Nodo2.Nodo2()
		nuevo.valor = valor
		if self.inicio == None:
			self.inicio = nuevo
		else:
			auxiliar = self.inicio
			while auxiliar.siguiente != None:
				auxiliar = auxiliar.siguiente
			auxiliar.siguiente = nuevo
			nuevo.anterior = auxiliar
	def eliminar(self,valor):
		if self.inicio != None:
			auxiliar = self.inicio
			anterior = None
			while auxiliar != None:
				if auxiliar.valor == valor:
					if anterior == None:
						self.inicio = self.inicio.siguiente
						auxiliar.siguiente = None
						auxiliar = self.inicio
					else:
						anterior.siguiente = auxiliar.siguiente
						auxiliar.siguiente = None
						auxiliar = anterior.siguiente
				else:
					anterior = auxiliar
					auxiliar = auxiliar.siguiente
	def recorrerLista(self):
		auxiliar = self.inicio
		while auxiliar != None:
			print (auxiliar.valor)
			auxiliar = auxiliar.siguiente
listadoble = ListaDoble()
listadoble.insertarFinal(2)
listadoble.insertarFinal(2)
listadoble.insertarFinal(3)
listadoble.insertarFinal(4)
listadoble.insertarFinal(5)
listadoble.insertarFinal(10)
listadoble.recorrerLista()


					
	