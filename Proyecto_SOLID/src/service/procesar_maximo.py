from service.interfaces.i_procesar_maximo import IProcesarMaximo


class ProcesarMaximo(IProcesarMaximo):
    def procesar(self, datos):
        return max(datos)