#!/usr/bin/python

import webapp
import urllib

class proxy(webapp.webApp):

	dicc = {}
	
	def ponehello(self, contenido):
		posicion1 = contenido.find("<body>")
		posicion2 = contenido.find(">", posicion1) 
		return contenido[:(posicion2+1)] + "Holaaa!!-" + contenido[(posicion2 + 1):]

	def poneroriginal(self, contenido, pag):
		posicion1 = contenido.find("<body")
		posicion2 = contenido.find(">",posicion1)
		return contenido[:(pos2+1)] + "<a href='" + pag +"'>url original-</a>" + contenido[(pos2+1):]


	def ponerecarga(self, contenido, parsedRequest):
		posicion1 = contenido.find("<body")
		posicion2 = contenido.find(">",pos1)
		return contenido[:(pos2+1)] +"<a href='" + "http://localhost:1234/" + parsedRequest +"'>recargar-</a>" + "<br>" + contenido[(pos2+1):]

	def guardarcache(self, parsedRequest):
		posicion1 = parsedRequest.find(".")
		pk = parsedRequest[:pos1]
		self.cache[pk] = "<a href='http://" + parsedRequest + "'>'http://'" + parsedRequest + "</a>"

	def insertarcache(self, contenido):
		posicion1 = contenido.find("<body")
		posicion2 = contenido.find(">",pos1)
		return contenido[:(posicion2+1)] + str(self.cache)+ "<br>" + contenido[(posicion2+1):]

	def parse(self, request):
		try:
			url = str(request.split("/")[1][: -4])
			return url
		except:
			return None

	def process(self,  parsedRequest):
		try:
			pag = urllib.urlopen("http://" + parsedRequest)
			self.guardarcache(parsedRequest)
			contenido = pag.read()
			contenido = self.insertarcache(contenido)
			contenido = self.ponerecarga(contenido,parsedRequest)
			contenido = self.poneroriginal(contenido,"http://" + parsedRequest)
			contenido = self.ponertello(contenido)
			return ("200 OK", "<html><body><h1>" + contenido + "</h1></body></html>")
		except IOError:
			return("400 Error", "")

if __name__ == "__main__":
	web = proxy("localhost", 1234)

