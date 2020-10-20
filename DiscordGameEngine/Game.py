import random
from PIL import Image




class ClientGame:
    def __init__(self, png, x = 0, y = 0, other = []):
        self.x = x
        self.y = y
        self.other = other
        self.png = png

        self.pngimage = Image.open(png)

        self.getservping = False
        self.sendservping = False

    def start(self):
        self.sendservping = True



class ServerGame:
    def __init__(self, scenelist, charecterlist):
        self.scenes = scenelist
        self.charecters = charecterlist
        self.active = False
        self.LetterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                           "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.code = "######"


        self.save = []

    def setup(self):
        self.code = self.LetterList[random.randint(0, len(self.LetterList) - 1)] + \
                    self.LetterList[random.randint(0, len(self.LetterList) - 1)] + \
                    self.LetterList[random.randint(0, len(self.LetterList) - 1)] + \
                    self.LetterList[random.randint(0, len(self.LetterList) - 1)] + \
                    self.LetterList[random.randint(0, len(self.LetterList) - 1)] + \
                    self.LetterList[random.randint(0, len(self.LetterList) - 1)]
        self.active = True
        return self.code

    def start(self):
        pass

    def end(self):
        self.code = "######"
        self.active = False
