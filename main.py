import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
        self._configurar_argumentos()

    def _configurar_argumentos(self):
        self.parser.add_argument("--biblioteca", choices=["Matplotlib", "OpenCV"], required=True, help="Biblioteca para procesamiento de imagenes")
        self.parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")

    def parse_args(self):
        return self.parser.parse_args()

class ProcesamientoImagenes:
    def __init__(self, args):
        self.args = args

    def procesar(self):
        if self.args.biblioteca == 'OpenCV':
            from opencv_processor import OpenCVImageProcessor
            image_procesor = OpenCVImageProcessor()
        elif self.args.biblioteca == 'Matplotlib':
            from matplotlib_processor import MatplotlibImageProcessor
            image_procesor = MatplotlibImageProcessor()
        else:
            print("Biblioteca no valida. Selecciona PIL, Matplotlib o OpenCV.")
            return

        try:
            image_procesor.mostrar_imagen(self.args.imagen)
        except Exception as e:
            print(f"Error al procesar la imagen: {e}")

def main():
    argument_parser = ArgumentParser()
    args = argument_parser.parse_args()

    procesamiento = ProcesamientoImagenes(args)
    procesamiento.procesar()

if __name__ == "__main__":
    main()

