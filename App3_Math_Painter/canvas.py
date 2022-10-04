from PIL import Image
import numpy as np


class Canvas:
    """Object where all shapes will be drawn."""

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change [0, 0, 0] to user given value for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file."""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
