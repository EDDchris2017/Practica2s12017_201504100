import NodoMatriz

class Matriz:
	def __init__(self):
		self.dominioraiz = None
		self.letraraiz = None
		self.raiz = NodoMatriz.NodoMatriz()
		self.raiz.tipo = "principal"
	def obtenerPosicion(self,nombre):
		valor = 0
		letra_nombre = nombre[0]
		
		if letra_nombre == "a" or letra_nombre == "A":
			
			valor = 1
		elif letra_nombre == "b" or letra_nombre == "b":
			valor = 2
		elif letra_nombre == "c" or letra_nombre == "C":
			valor = 3
		elif letra_nombre == "d" or letra_nombre == "D":
			valor = 4
		elif letra_nombre == "e" or letra_nombre == "e":
			valor = 5
		elif letra_nombre == "f" or letra_nombre == "F":
			valor = 6
		elif letra_nombre == "g" or letra_nombre == "G":
			valor = 7
		elif letra_nombre == "h" or letra_nombre == "H":
			valor = 8
		elif letra_nombre == "i" or letra_nombre == "I":
			valor = 9
		elif letra_nombre == "j" or letra_nombre == "J":
			valor = 10
		elif letra_nombre == "k" or letra_nombre == "K":
			valor = 11
		elif letra_nombre == "l" or letra_nombre == "L":
			valor = 12
		elif letra_nombre == "m" or letra_nombre == "M":
			valor = 13
		elif letra_nombre == "n" or letra_nombre == "N":
			valor = 14
		elif letra_nombre == "ñ" or letra_nombre == "Ñ":
			valor = 15
		elif letra_nombre == "o" or letra_nombre == "O":
			valor = 16
		elif letra_nombre == "p" or letra_nombre == "P":
			valor = 17
		elif letra_nombre == "q" or letra_nombre == "Q":
			valor = 18
		elif letra_nombre == "r" or letra_nombre == "R":
			valor = 19
		elif letra_nombre == "s" or letra_nombre == "S":
			valor = 20	
		elif letra_nombre == "t" or letra_nombre == "T":
			valor = 21
		elif letra_nombre == "u" or letra_nombre == "U":
			valor = 22
		elif letra_nombre == "v" or letra_nombre == "V":
			valor = 23	
		elif letra_nombre == "w" or letra_nombre == "W":
			valor = 24
		elif letra_nombre == "x" or letra_nombre == "X":
			valor = 25
		elif letra_nombre == "y" or letra_nombre == "Y":
			valor = 26
		elif letra_nombre == "z" or letra_nombre == "Z":
			valor = 27	
		
		return valor
	def nohayDominios(self):
		condicion = False
		if self.dominioraiz == None:
			condicion = True
		else:
			condicion = False
		return condicion
	def nohayLetras(self):
		if self.letraraiz == None:
			return True
		else:
			return False
	
	def existeDominio(self,dominio):
		encontrado = False
		if self.raiz.derecha == None:
			encontrado = False
		else:
			auxiliar = self.raiz
			while(auxiliar!=null):
				if auxiliar.dominio == dominio:
					encontrado = True
				auxiliar = auxiliar.derecha
		return encontrado
	
	def existeLetra(self,letra):
		encontrado = False
		if self.raiz.abajo == None:
			encontrado = False
		else:
			auxiliar = self.raiz.abajo
			while(auxiliar != None):
				if auxiliar.letra == letra:
					encontrado = True
			    auxiliar = auxiliar.abajo
		return encontrado		
	def buscarDominio(self,dominio):
		encontrado = None
		auxiliar = self.raiz.derecha
		salir = False
		while(auxiliar != None and salir == False):
			if auxiliar.dominio == dominio:
				encontrado = auxiliar
				salir = True
			auxiliar = auxiliar.derecha
		return encontrado	
	def buscarLetra(self,letra):
		encontrado = None
		auxiliar = self.raiz.abajo
		while(auxiliar != None):
			if auxiliar.letra == letra:
				encontrado = auxiliar
			auxiliar = auxiliar.abajo
		return encontrado		
	def insertarDominio(self,dominio):
		retornar_dominio = None
		nuevo_dominio = NodoMatriz.NodoMatriz()
		nuevo_dominio.dominio = dominio
		nuevo_dominio.tipo = "dominio"
		#condicion = self.nohayDominios()
		
		salir = False
		if self.raiz.derecha == None:
			self.raiz.derecha = nuevo_dominio
			self.raiz.derecha.izquierda = self.raiz

			
		else:
			auxiliar = self.raiz
			while(auxiliar != None and salir == False):
				if auxiliar.derecha == None:
					auxiliar.derecha = nuevo_dominio
					auxiliar.derecha.izquierda = auxiliar.derecha
					salir = True
				elif int(self.obtenerPosicion(nuevo_dominio.dominio)) < int(self.obtenerPosicion(auxiliar.derecha.dominio)):
					temporal_derecha = auxiliar.derecha
					auxiliar.derecha = nuevo_dominio
					auxiliar.derecha.derecha = temporal_derecha
					auxiliar.derecha.izquierda = auxiliar
					auxiliar.derecha.derecha.izquierda = auxiliar.derecha
					salir = True
				else:
					auxiliar = auxiliar.derecha
				
		#self.recorrerDominios()
		return retornar_dominio
	def insertarLetra(self,letra):
		retornar_letra = None
		nueva_letra = NodoMatriz.NodoMatriz()
		nueva_letra.letra = letra
		nueva_letra.tipo = "letra"
		#condicion = self.nohayDominios()
		
		salir = False

		
		if self.raiz.abajo == None:
			self.raiz.abajo = nueva_letra
			self.raiz.abajo.arriba = self.raiz
			
			
		else:
			auxiliar = self.raiz
			while(auxiliar != None and salir == False):

				if auxiliar.abajo == None:
					auxiliar.abajo = nueva_letra
					auxiliar.abajo.izquierda = auxiliar.abajo
					salir = True
				elif int(self.obtenerPosicion(nueva_letra.letra)) < int(self.obtenerPosicion(auxiliar.abajo.letra)):
					
					temporal_abajo = auxiliar.abajo
					auxiliar.abajo = nueva_letra
					auxiliar.abajo.abajo = temporal_abajo
					auxiliar.abajo.arriba = auxiliar
					auxiliar.abajo.abajo.arriba = auxiliar.abajo
					salir = True
				else:
					auxiliar = auxiliar.abajo
					
		#self.recorrerDominios()
		return retornar_letra

	def insertarMatriz(self,correo):
		nodo_dominio = None
		nodo_letra = None
		valores = correo.split('@')
		nombre = valores[0]
		dominio = valores[1]
		letra = nombre[0]
		haydominio = self.existeDominio(dominio)
		hayletra = self.existeLetra(letra)
		if self.haydominio == False:
			nodo_dominio == self.insertarDominio(dominio)
		else:
			nodo_dominio = self.buscarDominio(dominio)
		if self.hayletra == False:
			nodo_letra == self.insertarLetra(letra)
		else:
			nodo_letra = self.buscarLetra(letra)
			
		
		def insertarNombre(self,nombre,dominio,letra,nodo_dominio,nodo_letra):
			nuevo_nombre = NodoMatriz.NodoMatriz()
			nuevo_nombre.nombre = nombre
			nuevo_nombre.letra = letra
			nuevo_nombre.dominio = dominio
			
			nododominio = 	buscarNombreenDominio(self,nodo_dominio,nuevo_nombre.letra):
			nodoletra =  buscarNombreenLetra(self,nodo_letra,nuevo_nombre.dominio):
			#Enganchar los nodos encontrados para nombre
			temporal_derecha = nodoletra.derecha
			temporal_arriba = nododominio.arriba
		
	def recorrerDominios(self):
		auxiliar = self.raiz
		while (auxiliar != None):
			print (auxiliar.dominio)
			print (auxiliar.letra)
			auxiliar = auxiliar.derecha
			
	def buscarNombreenDominio(self,nodo_dominio,nuevo_nodo_letra):
		retornar = None
		auxiliar = nodo_dominio
		while(auxiliar != None):
			if auxiliar.abajo ==None:
				retornar = auxiliar
			elif  self.obtenerPosicion(nuevo_nodo_letra) < self.obtenerPosicion(auxiliar.abajo.letra)
				retornar = auxiliar
			elif self.obtenerPosicion(nuevo_nodo_letra) = self.obtenerPosicion(auxiliar.abajo.letra)
				retornar = auxiliar.abajo
			else:
				auxiliar = auxiliar.abajo
	def buscarNombreenLetra(self,nodo_letra,nuevo_nodo_dominio):
		retornar = None
		auxiliar = nodo_letra
		while(auxiliar != None):
			if auxiliar.derecha ==None:
				retornar = auxiliar
			elif  self.obtenerPosicion(nuevo_nodo_dominio) < self.obtenerPosicion(auxiliar.derecha.dominio)
				retornar = auxiliar
			elif self.obtenerPosicion(nuevo_nodo_dominio) = self.obtenerPosicion(auxiliar.derecha.dominio)
				retornar = auxiliar.derecha
			else:
				auxiliar = auxiliar.derecha			
				
matriz = Matriz()
matriz.insertarDominio("a")

matriz.insertarDominio("r")
matriz.insertarDominio("d")
matriz.insertarDominio("z")
matriz.insertarLetra("a")
matriz.insertarLetra("r")
matriz.insertarLetra("c")
matriz.recorrerDominios()
busqueda = matriz.buscarLetra("k")
print ("dominio encontrado",busqueda.dominio)

	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		