from abc import ABC, abstractmethod

class IAlmacenamientoArchivo(ABC):
    @abstractmethod
    def guardar(self, contenido):
        pass