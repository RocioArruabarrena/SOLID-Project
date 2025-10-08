from service.interfaces.i_procesar_datos import IProcesarDatos


class ProcesarPromedio(IProcesarDatos):
    def procesar(self, datos):
        return sum(datos) / len(datos)

class ProcesarMaximo(IProcesarDatos):
    def procesar(self, datos):
        return max(datos)

class ProcesarMinimo(IProcesarDatos):
    def procesar(self, datos):
        return min(datos)


class ProcesadorEstrategia:
    def __init__(self, estrategia: IProcesarDatos):
        self.estrategia = estrategia

    def ejecutar(self, datos):
        return self.estrategia.procesar(datos)
