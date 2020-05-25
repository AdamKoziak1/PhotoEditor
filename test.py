from Cimpl import *

HEIGHT = 1000
WIDTH = 1400
SCALE = 150

image = create_image(WIDTH, HEIGHT, (0, 0, 0))

def draw_lines():
    for pixel in image:
        x, y, (r, g, b) = pixel
        
        if x % SCALE == 0:
            set_color(image, x, y, create_color(100,100,100))
        if y % SCALE == 0:
            set_color(image, x, y, create_color(100,100,100))  
            
        if y == HEIGHT/2:
            set_color(image, x, y, create_color(255,255,255))  
        if x == WIDTH/2:
            set_color(image, x, y, create_color(255,255,255))
   

'''    
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
m = (y2-y1) / (x2-x1)        
'''

draw_lines()

def cosine(x):
    return SCALE*math.cos(2*math.pi*(x-(WIDTH/2))/SCALE)+HEIGHT/2

for x in range(1, WIDTH):
    set_color(image, x, cosine(x), create_color(255, 0, 0))
    
    delta = int(cosine(x+1)-cosine(x))
    
    for i in range(abs(delta)+1):
        set_color(image, x, cosine(x)+i, create_color(255, 0, 0))
            
show(image)