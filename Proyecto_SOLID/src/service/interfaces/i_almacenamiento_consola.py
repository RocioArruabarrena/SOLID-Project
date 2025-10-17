from abc import ABC, abstractmethod

class IAlmacenamientoConsola(ABC):
    @abstractmethod
    def guardar(self, contenido):
        pass
