import argparse

class ArgumentParser:
    """Esta clase realiza el procesamiento de los argumentos
    en la terminal por medio de la biblioteca Argparse
    
    Puede formatear los argumentos pasados al script para escoger
    que biblioteca se utilzará para el procesamiento de las imágenes 
    (OpenCV o Matplotlib)
    """
    def __init__(self):
        # Inicialización del procesamiento de argumentos
        self.parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
        self._configurar_argumentos()

    def _configurar_argumentos(self):
        """Define los argumentos pasados al script (biblioteca y ruta de la imagen).
            Incluye strings de ayuda para indicar que se debe colocar en cada argumento. 
        """
        
        # Los argumentos deben seguir la sintaxis:
        # --biblioteca <OpenCV o Matplotlib> --imagen <ruta de la imagen> 
        self.parser.add_argument("--biblioteca", choices=["Matplotlib", "OpenCV"], required=True, help="Biblioteca para procesamiento de imagenes")
        self.parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")

    def parse_args(self):
        """Realziza el procesamiento de los argumentos.

        Returns:
            args: Los argumentos procesados. 
        """ 
        return self.parser.parse_args()

class ProcesamientoImagenes:
    """Esta clase realiza el procesamiento de las imágenes, utilizando la biblioteca
       OpenCV o Matplotlib, dependiendo de los argumentos pasados al script. 
    """
    def __init__(self, args):
        # Incialización del procesamiento de imágenes 
        self.args = args

    def procesar(self):
        """ Procesa la imagen en la ruta indicada por medio de las bibliotecas OpenCV, 
        o Matplotlib. 

        Returns:
            Imagen: La ventana con la imagen desplegada con la biblioteca indicada. 
        """ 
        if self.args.biblioteca == 'OpenCV':
            # Importar clase correspondiente a OpenCV
            from opencv_processor import OpenCVImageProcessor
            image_procesor = OpenCVImageProcessor()
        elif self.args.biblioteca == 'Matplotlib':
            # Importar clase correspondiente a Matplotlib
            from matplotlib_processor import MatplotlibImageProcessor
            image_procesor = MatplotlibImageProcessor()
        else:
            print("Biblioteca no valida. Selecciona PIL, Matplotlib o OpenCV.")
            return

        try:
            # Mostrar imagen
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

