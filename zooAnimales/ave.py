from animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
    
    @classmethod
    def cantidadAves(cls):
        cantidadAves = 0
        for ave in cls._listado:
            cantidadAves += 1
        return cantidadAves
    
    def movimiento():
        return "volar"
    
    def crearHalcon( nombre, edad, genero):
        ave = Ave(nombre, edad, "montanas" , genero, "cafe glorioso")
        Ave._listado.append(ave)
        Ave.halcones += 1
        return ave

    def crearAguila( nombre, edad, genero):
        ave = Ave(nombre, edad, "montanas" , genero, "blanco y amarillo")
        Ave._listado.append(ave)
        Ave.aguilas += 1
        return ave
    
    @classmethod
    def  getListado(cls):
        return cls.listado
    
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setPelaje(self,colorPlumas):
        self._colorPlumas = colorPlumas

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