import numpy as np
import NodoDominio
import NodoLetra
import Nodo_Nombre
class MatrizDispersa:
	def __init__(self):
		self.dominio_inicio = None
		self.letra_inicio = None 
		self.tamaño_dominios = 0
		self.tamaño_letras = 0
		self.letras = array((a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z))
	def obtenerPosicion(self,nombre)
		letra_nombre = nombre[0]
		for x in range(0,len(self.letras):
			if (self.letras[i] == letra_nombre ):
				return x
	def nohayDominios(self):
		if self.dominio_inicio == None:
			return True
		else:
			return False
	def nohayLetras(self):
		if self.letra_inicio == None:
			return True
		else:
			return False
	def existeDominio(self,dominio):
		
	def insertarMatriz(self,correo):
		valores = correo.split("@")
		nombre = valores[0]
		dominio = valores[1]
		letra = nombre[0]
		nodo_dominio = insertarDominio(dominio)
		nodo_letra = insertarLetra(letra)
		insertarNombre(nombre,nodo_dominio,nodo_letra)
		
	def insertarDominio(self,dominio):
		nuevo_dominio = NodoDominio.NodoDominio()
		nuevo_dominio.dominio = dominio
		if nohayDominios() == True:
			self.dominio_inicio = nuevo_dominio
		else:
			auxiliar = self.dominio_inicio
			while(auxiliar.siguiente != None):
				if obtenerPosicion(auxiliar.dominio) > obtenerPosicion(nuevo_dominio.dominio):
					temp = auxiliar
					auxiliar = nuevo_dominio
					auxiliar.derecha = temp
					auxiliar.izquierda = temp.anterior
					auxiliar.derecha.izquierda = auxiliar
					auxiloar.derecha.derecha = temp.derecha
					
				else:
				auxiliar = auxiliar.derecha
		return auxiliar
			
	def insertarLetra(self,letra):
		nueva_letra = NodoLetra.NodoLetra()
		nueva_letra.letra = letra
		if nohayLetras() == True:
			self.letra_inicio = nueva_letra
		else:
			auxiliar = self.letra_inicio
			while(auxiliar.siguiente != None):
				if obtenerPosicion(auxiliar.letra) > obtenerPosicion(nuevo_dominio.letra):
					temp = auxiliar
					auxiliar = nueva_letra
					auxiliar.arriba = temp
					auxiliar.abajo = temp.abajo
					auxiliar.arriba.abajo = auxiliar
					auxiliar.arriba.arriba = temp.arriba
				else:
				auxiliar = auxiliar.arriba		
		return auxiliar
	
	def insertarNombre(self,nombre,nodo_dominio,nodo_letra):
		nuevo_nombre = Nodo_Nombre.NodoNombre()
		nuevo_nombre.nombre = nombre
		if nodo_dominio.abajo == None and nodo_letra.derecha = None:
			nodo_dominio.abajo = nuevo_nombre
			nodo_letra.derecha = nuevo_nombre
			nuevo_nombre.arriba = nodo_dominio
			nuevo_nombre.izquierda = nodo_letra
		else:
	def inserta		
			
	
		