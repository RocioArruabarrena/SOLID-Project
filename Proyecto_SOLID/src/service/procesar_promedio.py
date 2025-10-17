from service.interfaces.i_procesar_promedio import IProcesarPromedio

class ProcesarPromedio(IProcesarPromedio):
    def procesar(self, datos):
        return sum(datos) / len(datos)


