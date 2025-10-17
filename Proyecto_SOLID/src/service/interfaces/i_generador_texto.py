from abc import ABC, abstractmethod

class IGeneradorTexto(ABC):
    @abstractmethod
    def generar(self, resultado):
        pass
