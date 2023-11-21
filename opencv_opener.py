import cv2
from image_processor import ImageOpener

class OpenCVImageOpener(ImageOpener):

    def abrir_imagen(self, image_path):
        image = cv2.imread(image_path) # Lee la imagen

        # Muestra la imagen
        cv2.imshow('Imagen', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

