from service.interfaces.i_procesar_minimo import IProcesarMinimo

class ProcesarMinimo(IProcesarMinimo):
    def procesar(self, datos):
        return min(datos)
