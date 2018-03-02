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
            if not grid[i[1]+y][i[0]+x]: t1+=str(ind)
            ind += 1
        if t1: t2 = eval(r'"\N{Braille Pattern Dots-%s}"' % t1)
        else: t2 = chr(10240) #eval(r'"\N{Braille Pattern Dots-%s}"' % '3')
        c += t2

    f += c+'\n'

print(f)
img.show()



##import dither
##from PIL import Image
##
##img = Image.open("kittensmall.png")
##dither.floydDither(img,((0,0,0),(255,255,255)))
###img.show()
##w = img.width
##h = img.height
##print(h)
##w += (w%2)
##if h%3 != 0: h += (3-h%3)
##nimg = Image.new('RGB',(w,h),color=(255,255,255))
##nimg.paste(img)
##grid = []
##
##for y in range(h):
##    col = []
##    for x in range(w):
##        p = nimg.getpixel((x,y))
##        if p[0]:
##            col.append(0)
##        else:
##            col.append(1)
##    grid.append(col)
##
##for y in range(h):
##    p = ''
##    for x in range(w):
##        if grid[x][y]:
##            p += '⠿'
##        else: p += '⠄'
##    print(p)
##
##finalText = ''
##for y in range(0,h,3): 
##    for x in range(0,w,2):
##        surround = ''
##        try:
##            surround += str(bool(grid[x][y]))[0].lower()
##            surround += str(bool(grid[x + 1][y]))[0].lower()
##            surround += str(bool(grid[x][y + 1]))[0].lower()
##            surround += str(bool(grid[x + 1][y + 1]))[0].lower()
##            surround += str(bool(grid[x][y + 2]))[0].lower()
##            surround += str(bool(grid[x + 1][y + 2]))[0].lower()
##        except:
##            print(surround)
##            print(x)
##            print(y)
##            break
##        if surround == 'ffffff':
##            finalText += '⠀'
##            break
##        elif surround == 'tfffff':
##            finalText += '⠁'
##            break
##        elif surround == 'fftfff':
##            finalText += '⠂'
##            break
##        elif surround == 'tftfff':
##            finalText += '⠃'
##            break
##        elif surround == 'fffftf':
##            finalText += '⠄'
##            break
##        elif surround == 'tffftf':
##            finalText += '⠅'
##            break
##        elif surround == 'fftftf':
##            finalText += '⠆'
##            break
##        elif surround == 'tftftf':
##            finalText += '⠇'
##            break
##        elif surround == 'ftffff':
##            finalText += '⠈'
##            break
##        elif surround == 'ttffff':
##            finalText += '⠉'
##            break
##        elif surround == 'fttfff':
##            finalText += '⠊'
##            break
##        elif surround == 'tttfff':
##            finalText += '⠋'
##            break
##        elif surround == 'ftfftf':
##            finalText += '⠌'
##            break
##        elif surround == 'ttfftf':
##            finalText += '⠍'
##            break
##        elif surround == 'fttftf':
##            finalText += '⠎'
##            break
##        elif surround == 'tttftf':
##            finalText += '⠏'
##            break
##        elif surround == 'ffftff':
##            finalText += '⠐'
##            break
##        elif surround == 'tfftff':
##            finalText += '⠑'
##            break
##        elif surround == 'ffttff':
##            finalText += '⠒'
##            break
##        elif surround == 'tfttff':
##            finalText += '⠓'
##            break
##        elif surround == 'fffttf':
##            finalText += '⠔'
##            break
##        elif surround == 'tffttf':
##            finalText += '⠕'
##            break
##        elif surround == 'fftttf':
##            finalText += '⠖'
##            break
##        elif surround == 'tftttf':
##            finalText += '⠗'
##            break
##        elif surround == 'ftftff':
##            finalText += '⠘'
##            break
##        elif surround == 'ttftff':
##            finalText += '⠙'
##            break
##        elif surround == 'ftttff':
##            finalText += '⠚'
##            break
##        elif surround == 'ttttff':
##            finalText += '⠛'
##            break
##        elif surround == 'ftfttf':
##            finalText += '⠜'
##            break
##        elif surround == 'ttfttf':
##            finalText += '⠝'
##            break
##        elif surround == 'fttttf':
##            finalText += '⠞'
##            break
##        elif surround == 'tttttf':
##            finalText += '⠟'
##            break
##        elif surround == 'ffffft':
##            finalText += '⠠'
##            break
##        elif surround == 'tfffft':
##            finalText += '⠡'
##            break
##        elif surround == 'fftfft':
##            finalText += '⠢'
##            break
##        elif surround == 'tftfft':
##            finalText += '⠣'
##            break
##        elif surround == 'fffftt':
##            finalText += '⠤'
##            break
##        elif surround == 'tffftt':
##            finalText += '⠥'
##            break
##        elif surround == 'fftftt':
##            finalText += '⠦'
##            break
##        elif surround == 'tftftt':
##            finalText += '⠧'
##            break
##        elif surround == 'ftffft':
##            finalText += '⠨'
##            break
##        elif surround == 'ttffft':
##            finalText += '⠩'
##            break
##        elif surround == 'fttfft':
##            finalText += '⠪'
##            break
##        elif surround == 'tttfft':
##            finalText += '⠫'
##            break
##        elif surround == 'ftfftt':
##            finalText += '⠬'
##            break
##        elif surround == 'ttfftt':
##            finalText += '⠭'
##            break
##        elif surround == 'fttftt':
##            finalText += '⠮'
##            break
##        elif surround == 'tttftt':
##            finalText += '⠯'
##            break
##        elif surround == 'ffftft':
##            finalText += '⠰'
##            break
##        elif surround == 'tfftft':
##            finalText += '⠱'
##            break
##        elif surround == 'ffttft':
##            finalText += '⠲'
##            break
##        elif surround == 'tfttft':
##            finalText += '⠳'
##            break
##        elif surround == 'fffttt':
##            finalText += '⠴'
##            break
##        elif surround == 'tffttt':
##            finalText += '⠵'
##            break
##        elif surround == 'fftttt':
##            finalText += '⠶'
##            break
##        elif surround == 'tftttt':
##            finalText += '⠷'
##            break
##        elif surround == 'ftftft':
##            finalText += '⠸'
##            break
##        elif surround == 'ttftft':
##            finalText += '⠹'
##            break
##        elif surround == 'ftttft':
##            finalText += '⠺'
##            break
##        elif surround == 'ttttft':
##            finalText += '⠻'
##            break
##        elif surround == 'ftfttt':
##            finalText += '⠼'
##            break
##        elif surround == 'ttfttt':
##            finalText += '⠽'
##            break
##        elif surround == 'fttttt':
##            finalText += '⠾'
##            break
##        elif surround == 'tttttt':
##            finalText += '⠿'
##            break
##    finalText += '\n'
##
##print(finalText)
