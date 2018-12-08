from PIL import Image
import dither

img = Image.open("kittensmall.png")
dither.floydDither(img,((0,0,0),(255,255,255)))

w = img.width
h = img.height

w += (w%2)
if h%3 != 0: h += (3-h%3)
print(w,h)

nimg = Image.new('RGB',(w,h),color=(255,255,255))
nimg.paste(img)
img = nimg.copy()
del nimg

grid = []

for y in range(h):
    col = []
    for x in range(w):
        p = img.getpixel((x,y))
        if p[0]:
            col.append(0)
        else:
            col.append(1)
    grid.append(col)


checks = ([0,0],[0,1],[0,2],[1,0],[1,1],[1,2])

f = ''
for y in range(0,h,3):
    c = ''
    for x in range(0,w,2):
        t1 = ''
        ind = 1
        for i in checks:
            if not grid[i[1]+y][i[0]+x]: t1+=str(ind) # remove not if u want reverse thing blablaa
            ind += 1
        if t1: t2 = eval(r'"\N{Braille Pattern Dots-%s}"' % t1)
        else: t2 = chr(10240) #eval(r'"\N{Braille Pattern Dots-%s}"' % '3')
        c += t2

    f += c+'\n'

print(f)
img.show()
