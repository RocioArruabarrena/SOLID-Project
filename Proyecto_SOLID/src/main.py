from controller.reporte_controller import ReporteController

def main():
    controller = ReporteController()
    controller.ejecutar_reporte_promedio()
    controller.ejecutar_reporte_maximo()

if __name__ == "__main__":
    main()

