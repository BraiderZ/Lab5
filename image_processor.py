from abc import ABC, abstractmethod

class ImageProcessor(ABC):
    @abstractmethod
    def mostrar_imagen(self, image_path):
        pass

    @abstractmethod
    def procesar(self, image_path):
        pass

