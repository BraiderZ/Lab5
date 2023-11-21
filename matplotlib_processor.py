import matplotlib.pyplot as plt
from matplotlib.image import imread

class MatplotlibImageProcessor():
    def mostrar_imagen(self, image_path):
        image = imread(image_path)
        plt.imshow(image)
        plt.axis('off')
        plt.show()

