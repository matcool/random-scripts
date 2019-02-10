import pygame, sys
from pygame.locals import *
import keyboard

KEYC = 200,200,200
BACKGROUNDC = 0,0,100

class key:
	def __init__(self,hotkey,x,y,text=None,w=60,h=60):
		self.key = hotkey
		self.x = x
		self.y = y
		if text is None: self.text = self.key
		else: self.text = text
		self.fontimg = font.render(self.text,1,(255,255,255))
		self.w = w
		self.h = h

	def draw(self):
		pygame.draw.rect(screen, KEYC, (self.x,self.y,self.w,self.h),0 if keyboard.is_pressed(self.key) else 3)
		screen.blit(self.fontimg,(self.x+self.w//2-self.fontimg.get_width()//2,self.y+self.h//2-self.fontimg.get_height()//2))

size = width, height = 500, 200
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("mat's very original board")
pygame.init()
font = pygame.font.Font(None, 35)

keys = [
	key('left',5,70,'<'),
	key('right',125,70,'>'),
	key('up',65,10,'^'),
	key('down',65,70,'v'),
	key('z',190,5),
	key('x',255,5),
	key('c',320,5),
	key('space',190,70,'',190),
]

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.display.quit()
			sys.exit(0)
		elif event.type == VIDEORESIZE:
			size = window,height = event.size
			screen = pygame.display.set_mode(size, pygame.RESIZABLE)

	screen.fill(BACKGROUNDC)
	for k in keys:
		k.draw()
	pygame.display.update() 