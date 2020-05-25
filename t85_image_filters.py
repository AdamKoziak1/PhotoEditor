'''
Milestone 2 (updated for milestone 3)
Group 85
31/03/2020
Adam Koziak, Joey Murphy, Henry Lin, Nguyen Gia Hieu Tu
'''

from Cimpl import *
from simple_Cimpl_filters import *

#red filter - Adam Koziak
def red_channel(original_image):
    '''
    Creates a new image from an original image with only red pixels being displayed
    '''
    red_copy = copy(original_image)
    for pixel in original_image: 
        x, y, (r,g,b) = pixel
        red = create_color(r,0,0)
        set_color(red_copy, x, y, red)
    return red_copy


#green filter - Adam Koziak
def green_channel(original_image):
    '''
    Creates a new image from an original image with only green pixels being displayed
    '''
    green_copy = copy(original_image)
    for pixel in original_image: 
        x, y, (r,g,b) = pixel
        green = create_color(0,g,0)
        set_color(green_copy, x, y, green)
    return green_copy


#blue filter - Adam Koziak
def blue_channel(original_image):
    '''
    Creates a new image from an original image with only blue pixels being displayed
    '''
    blue_copy = copy(original_image)
    for pixel in original_image: 
        x, y, (r,g,b) = pixel
        blue = create_color(0,0,b)
        set_color(blue_copy, x, y, blue)
    return blue_copy


#combine filter - Adam Koziak
def combine(red, green, blue):
    '''
    combines the rbg values into one image
    '''
    combined_image = copy(red)
    for pixel in combined_image: 
        x, y, (r,g,b) = pixel
        r = get_color(red, x, y)
        g = get_color(green, x, y)
        b = get_color(blue, x, y)
        rgb = create_color(r[0],g[1],b[2])
        set_color(combined_image, x, y, rgb)
    return combined_image


#two-tone filter - Adam Koziak
def two_tone(original_image, choice1, choice2):
    '''
    given two colors, it changes dark pixels to choice 1 and light pixels to choice2
    '''
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)
    
    colors = [black, white, red, lime, blue, yellow, cyan, magenta, gray]
    choices = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
    
    color1 = colors[choices.index(choice1)]
    color2 = colors[choices.index(choice2)]
    
    two_tone_copy = copy(original_image)
    for pixel in original_image: 
        x, y, (r,g,b) = pixel
        brightness = ((r + g + b)/3)
        if brightness <= 127:
            c = color1
        else:
            c = color2
        set_color(two_tone_copy, x, y, c)
    return two_tone_copy    


#three-tone filter - Adam Koziak
def three_tone(original_image, choice1, choice2, choice3):
    '''
    given three colors, it changes dark pixels to choice 1, medium pixels to choice 2, and light pixels to choice 3
    '''
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    red = create_color(255, 0, 0)
    lime = create_color(0, 255, 0)
    blue = create_color(0, 0, 255)
    yellow = create_color(255, 255, 0)
    cyan = create_color(0, 255, 255)
    magenta = create_color(255, 0, 255)
    gray = create_color(128, 128, 128)
    
    colors = [black, white, red, lime, blue, yellow, cyan, magenta, gray]
    choices = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
    
    color1 = colors[choices.index(choice1)]
    color2 = colors[choices.index(choice2)]
    color3 = colors[choices.index(choice3)]
    
    two_tone_copy = copy(original_image)
    for pixel in original_image: 
        x, y, (r,g,b) = pixel
        brightness = ((r + g + b)/3)
        if  brightness <= 84:
            c = color1
        elif 84 < brightness <= 170:
            c = color2
        else:
            c = color3
        set_color(two_tone_copy, x, y, c)
    return two_tone_copy    


#extreme contrast filter - Joey Murphy
def extreme_contrast(original_image)-> Image :
    """This function calls an image of the user's choice which then looks at each
    component of each pixel and if any component is less than or equal to 127
    than that component is set to 0 for that pixel on the new image. If the
    component is more than or equal to 128 than that component for the pixel is
    set to 255 on the new image.
    """    
    
    new_image = copy(original_image)

    #list for RGBs was implemented instead of multiple if statements for
    #each RGB component
    for pixel in original_image:
        x, y, (r, g, b) = pixel
        lst_rgb = [r ,g, b]
        lst_new_rgb = [0, 0, 0]
        for i in range (3):
            if lst_rgb[i] <= 127:
                lst_new_rgb[i] = 0
            else:
                lst_new_rgb[i] = 255
        new_color = create_color(lst_new_rgb[0], lst_new_rgb[1], lst_new_rgb[2])
        set_color (new_image, x, y, new_color)
    
    return new_image


#sepia tinting filter - Nguyen Gia Hieu Tu
def tinting(image :Image) -> Image:
    '''
    applies a sepia tint to a given image
    '''
    gray = grayscale(image)
    
    for pixel in gray:
        x, y, (r, g, b) = pixel
        
        
        if r <63:
            set_color(gray,x,y,create_color(r * 1.1, g,b * 0.9))
            
        if 63 <= r and r <= 191:          
            set_color(gray,x,y,create_color(r * 1.15, g,b * 0.85) )
            
        if r > 191:        
            set_color(gray,x,y,create_color(r * 1.08, g,b * 0.93))
            
    return gray


#posterize filter and adjust_component helper method - Henry Lin
def _adjust_component(component: int) -> int:
    """Return the midpoint of the quadrant of the range 0-255 that the given 
    component belongs to. Each quadrant spans 63 integers, and the midpoints 
    are: 31, 95, 159, 223.
    >>> _adjust_component(25)
    31
    >>> _adjust_component(115)
    95
    """
    if component <= 63:
        return 31
    elif component > 63 and component <= 127:
        return 95
    elif component > 127 and component <= 191:
        return 159
    else: #component > 191
        return 223

def posterize(image: Image) -> Image:
    """Return a copy of the image where all pixels' R, G, and B components are 
    set to the midpoint of the quadrant of the range 0-255 they lie in.
    >>> copy = posterize(image)
    >>> show(copy)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        set_color(new_image, x, y, create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b)))
    return new_image
    

#vertical flip filter- Adam Koziak
def flip_vertical(original):
    flipped = copy(original)
    width = get_width(original)
    for pixel in original:
        x, y, (r, g, b) = pixel
        col = create_color(r, g, b)
        x2 = width-x-1
        set_color(flipped, x2, y, col)
    return flipped    
    

#horizontal flip filter - Joey Murphy
def flip_horizontal (photo: str or Image) -> Image:
    """Return an image that has been flipped on an imaginary horizontal line in
    the middle of the picture from a given file name or an image.
     """
    if type(photo) == str:
        original_image = load_image(photo)
        
    else:
        original_image = photo
        
    image_new = copy(original_image)
    
    width = get_width (original_image) 
    height = get_height (original_image) -1
    
    if ((height + 1) % 2) == 0:
        horizontal_line = (height // 2) + 1
        
    else:
        horizontal_line = (height // 2)
        
    for x in range (width):
        y1 = 0
        y2 = height 
        while y1 != horizontal_line:
            
            (r1, g1, b1) = get_color (original_image, x, y1)
            (r2, g2, b2) = get_color (original_image, x, y2)
            
            set_color (image_new, x, y1, create_color(r2, g2, b2))
            set_color (image_new, x, y2, create_color(r1, g1, b1))  
            
            y1 += 1
            y2 -= 1
            
    return image_new


#edge detection filter - Nguyen Gia Hieu Tu
def detect_edges( original_image : Image, threshold : int ) -> Image:
    ''' Return a copy of an image, which has been applied with a filter look like a pencil sketch piture
    '''
    new_image = copy( original_image )
    for h in range ( 1, get_height (new_image) -1 ):
        for w in range ( 1 , get_width (new_image) -1 ):
            
            top_red, top_green, top_blue = get_color (new_image,w, h - 1)
            bottom_red, bottom_green, bottom_blue = get_color (new_image,w, h + 1)
            
            brightness_top = (top_red + top_green + top_blue) // 3
            brightness_bottom = (bottom_red + bottom_green + bottom_blue) // 3
            
            brightness = abs(brightness_top - brightness_bottom)
            
            if brightness > threshold:
                new_color = create_color (0,0,0)
            else:
                new_color = create_color (255,255,255)
            
            set_color (new_image , w , h-1 , new_color)
            
    return new_image


#improved edge detection filter - Henry Lin
def detect_edges_better( original_image : Image, threshold : int ) -> Image:
    """Return a copy of the image that has been modified using a simple edge 
    detection algorithm, which changes each pixel to black or white depending 
    on the contrast between the pixel and its neighbours to the right and below.
    >>> filtered_img = detect_edges_better(image)
    >>> show(filtered_img)
    """
    new_image = copy( original_image )
    for h in range ( 1, get_height (new_image) -1 ):
        for w in range ( 1 , get_width (new_image) -1 ):
            top_red, top_green, top_blue = get_color (new_image,w, h - 1)
            bottom_red, bottom_green, bottom_blue = get_color (new_image,w, h + 1)
            right_red, right_green, right_blue = get_color (new_image, w + 1, h)
            
            brightness_top = (top_red + top_green + top_blue) // 3
            brightness_bottom = (bottom_red + bottom_green + bottom_blue) // 3
            brightness_right = (right_red + right_green + right_blue) // 3
            contrast_bottom = abs(brightness_top - brightness_bottom)
            contrast_right = abs(brightness_top - brightness_right)
            
            if contrast_bottom > threshold or contrast_right > threshold:
                new_color = create_color (0,0,0)
            else:
                new_color = create_color (255,255,255)
            
            set_color (new_image , w , h-1 , new_color)
            
    return new_image