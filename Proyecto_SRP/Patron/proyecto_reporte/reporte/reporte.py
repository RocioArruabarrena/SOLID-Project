class Reporte:
    def __init__(self, fuente, procesador_estrategia, generador, almacenamiento):
        self.fuente = fuente
        self.procesador_estrategia = procesador_estrategia
        self.generador = generador
        self.almacenamiento = almacenamiento

    def ejecutar(self):
        datos = self.fuente.obtener_datos()
        resultado = self.procesador_estrategia.ejecutar(datos)
        salida = self.generador.generar(resultado)
        self.almacenamiento.guardar(salida)

