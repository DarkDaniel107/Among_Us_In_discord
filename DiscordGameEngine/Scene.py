import PIL
from PIL import Image


class State:
    def __init__(self, hitboxes, ImageDirectory, Name):
        self.name = Name
        self.hitboxes = hitboxes
        self.image = Image.open(ImageDirectory)
