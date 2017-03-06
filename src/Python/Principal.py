import ListaSimple
import Pila
import Cola
from flask import Flask, request, Response
import os
app = Flask("EDD_codigo_ejemplo")

class Principal():
	def __init__(self):
		self.cola = Cola.Cola()
		self.pila = Pila.Pila()
		self.lista = ListaSimple.ListaSimple()
	
	def insertarCola(self,valor):
			self.cola.insertar(valor)
			print ("inserto en la cola")
	
	def ingresarCola():
		valor =  str(request.form['valor_cola'])
		self.cola.insertar(valor)
		return ("ingreso valor en cola")

principal = Principal()	
@app.route('/ingresarCola',methods=['POST']) 
def ingresarCola():
	valor = int(request.form['valor_cola'])
	principal.insertarCola(valor)
	return ("inserto en la cola")
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')


