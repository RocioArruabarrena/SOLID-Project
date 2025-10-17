from service.interfaces.i_generador_json import IGeneradorJson

class GeneradorJSON(IGeneradorJson):
    def generar(self, resultado):
        return {"resultado": resultado}