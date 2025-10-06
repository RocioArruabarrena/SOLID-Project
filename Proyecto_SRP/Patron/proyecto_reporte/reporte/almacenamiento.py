from reporte.interfaces.i_almacenamiento import IAlmacenamiento

class AlmacenamientoArchivo(IAlmacenamiento):
    def guardar(self, contenido):
        with open("reporte.txt", "w") as f:
            f.write(str(contenido))

class AlmacenamientoConsola(IAlmacenamiento):
    def guardar(self, contenido):
        print("Reporte:", contenido)
