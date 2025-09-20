class Reporte:
    def __init__(self, fuente, procesador, generador, almacenamiento):
        self.fuente = fuente
        self.procesador = procesador
        self.generador = generador
        self.almacenamiento = almacenamiento

    def ejecutar(self):
        datos = self.fuente.obtener_datos()
        promedio = self.procesador.calcular_promedio(datos)
        salida = self.generador.generar(promedio)
        self.almacenamiento.guardar(salida)
