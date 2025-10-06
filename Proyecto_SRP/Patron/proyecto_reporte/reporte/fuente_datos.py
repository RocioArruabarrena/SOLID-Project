from reporte.interfaces.i_fuente_datos import IFuenteDeDatos

class FuenteDeDatosLista(IFuenteDeDatos):
    def obtener_datos(self):
        return [10, 20, 30, 40, 50]
