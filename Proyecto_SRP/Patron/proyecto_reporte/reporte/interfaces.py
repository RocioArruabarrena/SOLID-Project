from abc import ABC, abstractmethod

class IFuenteDeDatos(ABC):
    @abstractmethod
    def obtener_datos(self):
        pass

class IProcesarDatos(ABC):
    @abstractmethod
    def procesar(self, datos):
        pass

class IGeneradorSalida(ABC):
    @abstractmethod
    def generar(self, resultado):
        pass

class IAlmacenamiento(ABC):
    @abstractmethod
    def guardar(self, contenido):
        pass
