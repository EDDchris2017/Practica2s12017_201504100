import Nodo1
class Pila:
	def __init__(self):
		self.raiz = None
	def push(self,valor):
		nuevo = Nodo1.Nodo1()
		nuevo.valor = valor
		if self.raiz == None:
			nuevo.siguiente = None
			self.raiz = nuevo
		else:
			nuevo.siguiente = self.raiz
			self.raiz = nuevo
	def pop(self):
		retornar = Nodo1.Nodo1()
		if self.raiz != None:
			retornar.valor = self.raiz.valor
			self.raiz = self.raiz.siguiente
		return retornar
 
