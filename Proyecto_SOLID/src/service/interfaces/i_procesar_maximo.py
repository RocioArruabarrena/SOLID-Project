from abc import ABC, abstractmethod

class IProcesarMaximo(ABC):
    @abstractmethod
    def procesar(self, datos):
        pass