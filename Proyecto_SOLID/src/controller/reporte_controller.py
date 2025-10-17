from dao.fuente_datos import FuenteDeDatosLista
from service.procesar_promedio import ProcesarPromedio
from service.generador_texto import GeneradorTexto
from service.almacenamiento_archivo import AlmacenamientoArchivo
from service.reporte import Reporte
from service.procesar_estrategia import ProcesadorEstrategia
from service.procesar_maximo import ProcesarMaximo


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
