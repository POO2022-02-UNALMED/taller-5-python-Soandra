from zooAnimales.animal import Animal


class Pez(Animal):
	_listado = []
	salmones = 0
	bacalaos = 0

	def __init__(self,nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
		super().__init__(nombre, edad, habitat, genero)
		self._cantidadAletas = cantidadAletas
		self._colorEscamas = colorEscamas
		Pez._listado.append(self)

	def movimiento():
		return "nadar"

	@classmethod
	def crearSalmon(cls,nombre,edad,genero):
		cls.salmones+=1
		return Pez(nombre,edad,"oceano",genero,"rojo",6)

	@classmethod
	def crearBacalao(cls,nombre,edad,genero):
		cls.bacalaos+=1
		return Pez(nombre,edad,"oceano",genero,"gris",6)

	@classmethod
	def cantidadPeces(cls):
		return len(cls._listado)

	def getCantidadAletas(self):
		return self._cantidadAletas

	def setCantidadAletas(self,cantidadAletas):
		self._cantidadAletas = cantidadAletas

	def getColorEscamas(self):
		return self._colorEscamas

	def setColorEscamas(self,colorEscamas):
		self._colorEscamas = colorEscamas

	
	def getListado(cls):
		return cls._listado

	
	def setListado(cls,listado):
		cls._listado = listado