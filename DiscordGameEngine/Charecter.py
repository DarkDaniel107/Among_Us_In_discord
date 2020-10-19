from PIL import Image

class charecter:
    def __init__(self, x, y, PNGDirectory):
        self.x = x
        self.y = y
        self.PNG = Image.open(PNGDirectory)

