from abc import ABC, abstractmethod

class IAlmacenamiento(ABC):
    @abstractmethod
    def guardar(self, contenido):
        pass
