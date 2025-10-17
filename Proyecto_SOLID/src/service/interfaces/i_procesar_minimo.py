from abc import ABC, abstractmethod

class IProcesarMinimo(ABC):
    @abstractmethod
    def procesar(self, datos):
        pass