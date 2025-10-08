from service.fuente_datos import FuenteDeDatosLista
from service.procesar_datos import ProcesadorEstrategia, ProcesarPromedio, ProcesarMaximo
from service.generador_salida import GeneradorTexto
from service.almacenamiento import AlmacenamientoArchivo
from service.reporte import Reporte


class ReporteController:
    def __init__(self):
        self.fuente = FuenteDeDatosLista()
        self.estrategia = ProcesarPromedio()
        self.procesador = ProcesadorEstrategia(self.estrategia)
        self.generador = GeneradorTexto()
        self.almacenamiento = AlmacenamientoArchivo()

        self.reporte = Reporte(
            self.fuente,
            self.procesador,
            self.generador,
            self.almacenamiento
        )

    def ejecutar_reporte_promedio(self):
        print("Ejecutando reporte con promedio...")
        self.reporte.ejecutar()

    def ejecutar_reporte_maximo(self):
        print("\nCambiando estrategia a máximo...")
        self.procesador.estrategia = ProcesarMaximo()
        self.reporte.ejecutar()
