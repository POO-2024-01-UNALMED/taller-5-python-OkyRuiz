from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        cantidadReptiles = 0
        for reptil in cls._listado:
            cantidadReptiles += 1
        return cantidadReptiles

    def movimiento():
        return "reptar"
    
    def crearIguana( nombre, edad, genero):
        reptil = Reptil(nombre, edad, "humedal" , genero, "verdes", 3)
        Reptil._listado.append(reptil)
        Reptil.iguanas += 1
        return reptil

    def crearSerpiente( nombre, edad, genero):
        reptil = Reptil(nombre, edad, "jungla" , genero, "blanco", 1)
        Reptil._listado.append(reptil)
        Reptil.serpientes += 1
        return reptil
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self,largoCola):
        self._largoCola = largoCola

    def getNombre(self):
        return super().getNombre()
    
    def setNombre(nombre):
        super().setNombre(nombre)

    def getEdad(self):
        return super().getEdad()
    
    def setEdad(edad):
        super().setEdad(edad)

    def getHabitat(self):
        return super().getHabitat()
    
    def setHabitat(habitat):
        super().setHabitat(habitat)

    def getGenero(self):
        return super().getGenero()
    
    def setGenero(genero):
        super().setGenero(genero)