from abc import ABC, abstractmethod

class IProcesarPromedio(ABC):
    @abstractmethod
    def procesar(self, datos):
        pass
