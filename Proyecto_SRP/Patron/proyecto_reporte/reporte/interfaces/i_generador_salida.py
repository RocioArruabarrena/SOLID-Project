from abc import ABC, abstractmethod

class IGeneradorSalida(ABC):
    @abstractmethod
    def generar(self, resultado):
        pass
