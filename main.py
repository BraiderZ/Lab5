import argparse
from opencv_processor import OpenCVImageProcessor
from matplotlib_processor import MatplotlibImageProcessor

def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imágenes")
    parser.add_argument("--biblioteca", choices=["Matplotlib", "OpenCV"], required=True, help="Especifica la biblioteca de procesamiento de imágenes a utilizar.")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar.")
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        if args.biblioteca == 'Matplotlib':
            image_processor = MatplotlibImageProcessor()
        elif args.biblioteca == 'OpenCV':
            image_processor = OpenCVImageProcessor()
        else:
            raise ValueError("Biblioteca no válida. Selecciona Matplotlib u OpenCV.")

        image_processor.mostrar_imagen(args.imagen)
        image_processor.procesar(args.imagen)

    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

main()

