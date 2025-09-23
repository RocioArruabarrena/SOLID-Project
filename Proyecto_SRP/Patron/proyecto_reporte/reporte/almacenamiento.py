class Almacenamiento():
    def guardar_reporte(self, reporte):
        with open("reporte.txt", "w") as f:
            f.write(str(reporte))