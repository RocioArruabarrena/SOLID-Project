from abc import ABC, abstractmethod

class IProcesarEstrategia(ABC):
    @abstractmethod
    def procesar(self, datos):
        pass