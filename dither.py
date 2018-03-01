#the functions do the stuff on the pictures you give them
#instead of returning a new image

from PIL import Image,ImageDraw
import math
def closestColor(color,ColorList):
    ds = []
    for c in ColorList:
        d = math.pow(color[0]-c[0],2) + math.pow(color[1]-c[1],2) + math.pow(color[2]-c[2],2)
        ds.append(d)
    dss = ds.copy()
    dss.sort()
    return ColorList[ds.index(dss[0])]

def floydDither(img,colors):
    d = ImageDraw.Draw(img)
    for y in range(img.height):
        for x in range(img.width):
            oldC = img.getpixel((x,y))
            newC = closestColor(oldC,colors)
            d.point((x,y),fill=newC)
            errC = []
            for i in range(3):
                errC.append(oldC[i]-newC[i])
            errC = tuple(errC)
            indexes = [(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
            numbers = (7,5,3,1)
            for i in range(3):
                try:
                    c = img.getpixel(indexes[i])
                except IndexError:
                    continue
                color = []
                for sex in range(3):
                    color.append(int(c[sex] + errC[sex] * numbers[i]/16))
                color = tuple(color)
                d.point(indexes[i],fill=color)

def noDither(img,colors):
    d = ImageDraw.Draw(img)
    for y in range(img.height):
        for x in range(img.width):
            oldC = img.getpixel((x,y))
            newC = closestColor(oldC,colors)
            d.point((x,y),fill=newC)



