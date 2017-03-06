import Nodo1
class Cola:
	def __init__(self):
		self.raiz = None
		self.tamaño=0
		self.fondo = None
	def estaVacia(self):
		if self.raiz == None:
			return True
		else:
			return False
	def insertar(self,valor):
		nuevo = Nodo1.Nodo1()
		nuevo.valor = valor
		nuevo.siguiente = None
		condicion = self.estaVacia()
		if condicion == True:
			self.raiz = nuevo
			self.fondo = nuevo
		else:
			
			self.fondo.siguiente = nuevo
			self.fondo = self.fondo.siguiente
	def sacarCola(self):
		condicion = self.estaVacia()
		if condicion == False:
			dato = self.raiz
			if self.raiz == self.fondo:
				self.raiz = None
				self.fondo = None
			else:
				self.raiz = self.raiz.siguiente
		return dato		
