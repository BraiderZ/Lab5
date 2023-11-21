import matplotlib.pyplot as plt
import cv2
from image_processor import ImageProcessor

class MatplotlibImageProcessor(ImageProcessor):
    def mostrar_imagen(self, image_path):
        image = cv2.imread(image_path)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

    def procesar(self, image_path):

        # Agregar logica de la funcion procesar()
        
        pass
