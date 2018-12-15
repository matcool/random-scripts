from asciimatics.screen import Screen
from asciimatics.renderers import FigletText
from subprocess import run
from os import name as osname

def check():
    return not run('ping -{} 1 google.com'.format('n' if osname == 'nt' else 'c'), stdout=-3, shell=True).returncode

def getText(working):
    if working:
        status = 'YES!'
        footer = 'It works!'
        color = 2
    else:
        status = 'NO!'
        footer = 'Something\'s wrong'
        color = 1

    return {'status':status, 'footer':footer, 'color':color, 'height':6}

def main(screen):
    midW = int(screen.width/2)
    midH = int(screen.height/2)
    status = check()
    while True:
        ev = screen.get_key()
        if ev in (ord('r'), ord('R')):
            status,old = check(),status
            if old != status:
                screen.clear()
        elif ev in (ord('e'), ord('E')):
            return

        info = getText(status)
        figText = FigletText(info['status'], font='big')
        for y, i in enumerate(str(figText).splitlines()):
            if y == info['height']: break
            screen.print_at(i, midW-int(figText.max_width/2), y+midH-int(figText.max_height/2), colour=info['color'], attr=1)

        screen.print_at(info['footer'], midW-int(len(info['footer'])/2), y+1+midH-int(figText.max_height/2))
        screen.refresh()

Screen.wrapper(main)
