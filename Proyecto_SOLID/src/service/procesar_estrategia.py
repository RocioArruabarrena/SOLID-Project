from service.interfaces.i_procesar_estrategia import IProcesarEstrategia

class ProcesadorEstrategia:
    def __init__(self, estrategia: IProcesarEstrategia):
        self.estrategia = estrategia

    def ejecutar(self, datos):
        return self.estrategia.procesar(datos)