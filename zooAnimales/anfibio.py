from animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        cantidadAnfibios = 0
        for Anfibio in cls._listado:
            cantidadAnfibios += 1
        return cantidadAnfibios

    def movimiento():
        return "saltar"
    
    def crearRana( nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "selva" , genero, "rojo", True)
        Anfibio._listado.append(anfibio)
        Anfibio.ranas += 1
        return anfibio

    def crearSalamandra( nombre, edad, genero):
        anfibio = Anfibio(nombre, edad, "selva" , genero, "negro y amarillo", False)
        Anfibio._listado.append(anfibio)
        Anfibio.salamandras += 1
        return anfibio
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

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