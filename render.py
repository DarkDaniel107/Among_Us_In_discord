from PIL import Image
import os
from TEMP import Placer


def update(x, y, id=None):
    Map = Image.open("FullShip.png")
    # 1540x865
    # 770x430
    mutiplyer = 5
    Map = Map.resize((int(1540 * mutiplyer), int(865 * mutiplyer)))
    area = (x, y)
    area = (area[0] + 770, area[1] + 430)

    Map = Map.crop((area[0], area[1], area[0] + 1540, area[1] + 865))
    if id is None:
        im1 = Map.save("TEMP/GETMAPTESTTEMP.png", fb="/TEMP")
    else:
        im1 = Map.save("./TEMP/" + str(id) + "GETMAPTESTTEMP.png", fb="/TEMP")


def Render(ctx, x, y, serversavedata):
    if serversavedata == "VIEW":
        update(x, y, ctx.author.id)
        Needupdate = Image.open("./TEMP/" + str(ctx.author.id) + "GETMAPTESTTEMP.png")
        Player = Image.open("Lime.png")
        shrinkensize = 5
        Player = Player.resize((int(587/shrinkensize), int(744/shrinkensize)))
        # 770x430
        Size = Player.size
        Needupdate.paste(Player, (int(770-Size[0]/2), int(430-Size[1]/2)), mask=Player)
        Placer.place(Needupdate, ctx.author.id)
    else:
        update(x, y, ctx.author.id)
        Needupdate = Image.open("./TEMP/" + str(ctx.author.id) + "GETMAPTESTTEMP.png")
        Player = Image.open("Lime.png")
        shrinkensize = 5
        Player = Player.resize((int(587 / shrinkensize), int(744 / shrinkensize)))
        # 770x430
        Size = Player.size
        Needupdate.paste(Player, (int(770 - Size[0] / 2), int(430 - Size[1] / 2)), mask=Player)

        Placer.place(Needupdate, ctx.author.id)


def RemoveFrame(id = None):
    if id is None:
        os.remove("TEMP/GETMAPTESTTEMP.png")
    else:
        os.remove("TEMP/" + str(id) + "GETMAPTESTTEMP.png")
