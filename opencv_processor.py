import cv2
from image_processor import ImageProcessor

class OpenCVImageProcessor(ImageProcessor):
    def mostrar_imagen(self, image_path):
        image = cv2.imread(image_path)
        cv2.imshow('Imagen', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


