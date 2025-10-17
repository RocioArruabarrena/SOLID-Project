from service.interfaces.i_generador_texto import IGeneradorTexto

class GeneradorTexto(IGeneradorTexto):
    def generar(self, resultado):
        return f"Resultado del cálculo: {resultado}"
