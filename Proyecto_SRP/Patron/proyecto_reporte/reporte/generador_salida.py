from reporte.interfaces.i_generador_salida import IGeneradorSalida

class GeneradorTexto(IGeneradorSalida):
    def generar(self, resultado):
        return f"Resultado del cálculo: {resultado}"

class GeneradorJSON(IGeneradorSalida):
    def generar(self, resultado):
        return {"resultado": resultado}
