from abc import ABC, abstractmethod

class IGeneradorJson(ABC):
    @abstractmethod
    def generar(self, resultado):
        pass
