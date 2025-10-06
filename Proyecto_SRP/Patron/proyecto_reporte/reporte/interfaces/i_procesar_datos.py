from abc import ABC, abstractmethod

class IProcesarDatos(ABC):
    @abstractmethod
    def procesar(self, datos):
        pass
