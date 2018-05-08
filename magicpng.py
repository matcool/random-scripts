def mergeGetColor(px1,px2,lColor,dColor):
    A1 = getLum(px1)
    A2 = getLum(px2)
    R = weightedAverage(dColor[0],A1,lColor[0],A2)
    G = weightedAverage(dColor[1],A1,lColor[1],A2)
    B = weightedAverage(dColor[2],A1,lColor[2],A2)
    A = (A1+A2)/2
    return inttuple((R,G,B,A))

def getLum(px,inv=False,invBg=False):
    lum = (px[0]+px[1]+px[2])/3
    bgLum = 255
    if invBg != inv: bgLum = 0
    if inv: lum = 255-lum
    return weightedAverage(lum, px[3], bgLum, 255 - px[3])

def weightedAverage(val1,weight1,val2,weight2):
    if weight1+weight2 == 0:
        return (val1+val2) / 2

    return (val1*weight1 + val2*weight2) / (weight1+weight2)

def inttuple(t):
    return tuple([int(a) for a in t])

from PIL import Image
import sys
if len(sys.argv) == 1:
    import easygui
    img1 = easygui.fileopenbox()
    img2 = easygui.fileopenbox()
    del easygui
else:
    img1 = sys.argv[1] #input("Image 1:")
    img2 = sys.argv[2] #input("Image 2:")

del sys

img1 = Image.open(img1)
img2 = Image.open(img2)

if img1.size != img2.size:
    img2 = img2.resize(img1.size)

img1 = img1.convert("RGBA")
img2 = img2.convert("RGBA")
outimg = Image.new("RGBA",img1.size)
lcolor = (255,255,255)
dcolor = (54,57,62)

for x in range(img1.width):
    for y in range(img1.height):
        px1 = img1.getpixel((x,y))
        px2 = img2.getpixel((x,y))
        outimg.putpixel((x,y),mergeGetColor(px1,px2,lcolor,dcolor))

outimg.save("outputimage.png")
    
