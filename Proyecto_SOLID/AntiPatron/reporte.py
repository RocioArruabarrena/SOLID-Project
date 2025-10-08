class Reporte:
    def __init__(self):
        self.datos = []

    def obtener_datos(self):
        self.datos = [10, 20, 30, 40]

    def procesar_datos(self):
        #calculamos el promedio
        return sum(self.datos) / len(self.datos)

    def generar_salida(self, promedio):
        return {"promedio": promedio}

    def guardar_reporte(self, reporte):
        #guardamos en un archivo de texto
        with open("reporte.txt", "w") as f:
            f.write(str(reporte))

#usar
r = Reporte()
r.obtener_datos()
promedio = r.procesar_datos()
salida = r.generar_salida(promedio)
r.guardar_reporte(salida)
