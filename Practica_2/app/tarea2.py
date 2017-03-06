


from flask import Flask, request, Response
import os
app = Flask("__name__")


@app.route('/metodoNombre',methods=['POST']) 
def miNombre():
	parametro = str(request.form['p'])
	return "Christopher Alexander Lopez Orellana 201504100"

@app.route("/e")
def hellof():
	return "Hello World2!"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')