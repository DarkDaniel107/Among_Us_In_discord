import PIL
from PIL import Image


class Scene:
    def __init__(self, states):
        self.States = states


class State:
    def __init__(self, hitboxes, ImageDirectory, Name):
        self.name = Name
        self.hitboxes = hitboxes
        self.image = Image.open(ImageDirectory)
