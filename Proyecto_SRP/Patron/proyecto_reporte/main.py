from reporte.fuente_datos import FuenteDeDatosLista
from reporte.procesar_datos import ProcesadorEstrategia, ProcesarPromedio, ProcesarMaximo
from reporte.generador_salida import GeneradorTexto
from reporte.almacenamiento import AlmacenamientoArchivo
from reporte.reporte import Reporte

def main():
    fuente = FuenteDeDatosLista()
    estrategia = ProcesarPromedio()
    procesador = ProcesadorEstrategia(estrategia)

    generador = GeneradorTexto()
    almacenamiento = AlmacenamientoArchivo()

    reporte = Reporte(fuente, procesador, generador, almacenamiento)
    reporte.ejecutar()

    print("\nCambiando estrategia a máximo:")
    procesador.estrategia = ProcesarMaximo()
    reporte.ejecutar()

if __name__ == "__main__":
    main()
