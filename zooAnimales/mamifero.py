from animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
    @classmethod

    def cantidadMamiferos(cls):
        cantidadMamiferos = 0
        for mamifero in cls._listado:
            cantidadMamiferos += 1
        return cantidadMamiferos
    
    def crearCaballo( nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "pradera" , genero, True, 4)
        Mamifero._listado.append(mamifero)
        Mamifero.caballos += 1
        return mamifero

    def crearLeon( nombre, edad, genero):
        mamifero = Mamifero(nombre, edad, "selva" , genero, True, 4)
        Mamifero._listado.append(mamifero)
        Mamifero.leones += 1
        return mamifero
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self,pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas
    
    def setPatas(self,patas):
        self._patas = patas

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