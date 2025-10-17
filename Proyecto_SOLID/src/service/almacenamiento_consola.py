from service.interfaces.i_almacenamiento_consola import IAlmacenamientoConsola


class AlmacenamientoConsola(IAlmacenamientoConsola):
    def guardar(self, contenido):
        print("Reporte:", contenido)