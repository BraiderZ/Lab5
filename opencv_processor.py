import cv2

class OpenCVImageProcessor():
    """Esta clase realiza el procesamiento de imágenes por medio de 
    la biblioteca OpenCV.
    
    Puede mostrar imágenes en una nueva ventana.
    """
    def mostrar_imagen(self, image_path):
        """Muestra una imagen en una nueva ventana.

        Args:
            imagen_path (string): Ruta del archivo de la imagen que se desea abrir

        Returns:
            Imagen: La ventana con la imagen desplegada. 
        """
        image = cv2.imread(image_path)
        cv2.imshow('Imagen', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


