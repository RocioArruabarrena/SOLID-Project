from reporte.fuente_da import FuenteDeDatos
from reporte.process_datos import ProcesarDatos
from reporte.generador_salida import GeneradorSalida
from reporte.almacenamiento import Almacenamiento
from reporte.reporte import Reporte

def main():
    fuente = FuenteDeDatos()
    procesador = ProcesarDatos()
    generador = GeneradorSalida()
    almacenamiento = Almacenamiento()

    reporte = Reporte(fuente, procesador, generador, almacenamiento)
    reporte.ejecutar()

if __name__ == "__main__":
    main()
