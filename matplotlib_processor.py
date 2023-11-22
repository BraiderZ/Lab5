import matplotlib.pyplot as plt
from matplotlib.image import imread

class MatplotlibImageProcessor():
    """Esta clase realiza el procesamiento de imágenes por medio de 
    la biblioteca Matplotlib.
    
    Puede mostrar imágenes en una nueva ventana.
    """
    def mostrar_imagen(self, image_path):
        """Muestra una imagen en una nueva ventana.

        Args:
            imagen_path (string): Ruta del archivo de la imagen que se desea abrir

        Returns:
            Imagen: La ventana con la imagen desplegada.
        """ 
        image = imread(image_path)
        plt.imshow(image)
        plt.axis('off')
        plt.show()

