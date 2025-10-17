from abc import ABC, abstractmethod

class IFuenteDeDatos(ABC):
    @abstractmethod
    def obtener_datos(self):
        pass
