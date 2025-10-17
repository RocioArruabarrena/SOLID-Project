from service.interfaces.i_almacenamiento_archivo import IAlmacenamientoArchivo

class AlmacenamientoArchivo(IAlmacenamientoArchivo):
    def guardar(self, contenido):
        with open("reporte.txt", "w") as f:
            f.write(str(contenido))

