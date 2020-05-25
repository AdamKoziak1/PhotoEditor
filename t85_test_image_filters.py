from t85_image_filters import *
from Cimpl import *
from simple_Cimpl_filters import grayscale
from test_grayscale import check_equal

#red filter test - Adam Koziak
def test_red_channel(image) -> str:
    """Tests the function to make sure that it prints out only the 
    blue pixel of the image
    """
    passed = 0
    failed = 0    
    for pixel in image:
        x, y, (r, g, b) = pixel
        if (r != 0, g == 0, b == 0):
            passed += 1 
        else:
            failed += 1
    print("red filter test:", passed, "pixels passed, ", failed, "pixels failed")


#green filter test - Adam Koziak
def test_green_channel(image) -> str:
    """Tests the function to make sure that it prints out only the 
    blue pixel of the image
    """
    passed = 0
    failed = 0    
    for pixel in image:
        x, y, (r, g, b) = pixel
        if (r == 0, g != 0, b == 0):
            passed += 1 
        else:
            failed += 1
    print("green filter test:", passed, "pixels passed, ", failed, "pixels failed")


#blue filter test - Adam Koziak
def test_blue_channel(image) -> str:
    """Tests the function to make sure that it prints out only the 
    blue pixel of the image
    """
    passed = 0
    failed = 0    
    for pixel in image:
        x, y, (r, g, b) = pixel
        if (r == 0, g == 0, b != 0):
            passed += 1 
        else:
            failed += 1
    print("blue filter test:", passed, "pixels passed, ", failed, "pixels failed")


#combine filter test - Adam Koziak
def test_combine(original, combined) -> str:
    """Tests the combined image against the original to make sure RGB values match
    """
    passed = 0
    failed = 0      
    for pixel in original:
        x, y, (r, g, b) = pixel
        r2,g2,b2 = get_color(combined, x, y)
        if (r == r2, g != g2, b != b2):
            passed += 1
        else:
            failed += 1
    print("combine filter test:", passed, "pixels passed,", failed, "pixels failed")


#two-tone filter test - Adam Koziak
def two_tone_test(original, filtered, choice1, choice2):
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
    passed = 0
    failed = 0
    for pixel in original: 
        x, y, (r,g,b) = pixel
        brightness = ((r + g + b)/3)
        r2,g2,b2 = get_color(filtered, x, y)
        if brightness <= 127:
            if (r2,g2,b2) == color1:
                passed += 1
            else:
                failed += 1
        else:
            if (r2,g2,b2) == color2:
                passed += 1
            else:
                failed += 1
    print("two tone filter test:", passed, "pixels passed,", failed, "pixels failed")

#three-tone filter test - Adam Koziak
def three_tone_test(original, filtered, choice1, choice2, choice3):
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
    passed = 0
    failed = 0
    for pixel in original: 
        x, y, (r,g,b) = pixel
        brightness = ((r + g + b)/3)
        r2,g2,b2 = get_color(filtered, x, y)
        if brightness <= 84:
            if (r2,g2,b2) == color1:
                passed += 1
            else:
                failed += 1
        elif 84 < brightness <= 170:
            if (r2,g2,b2) == color2:
                passed += 1
            else:
                failed += 1
        else:
            if (r2,g2,b2) == color3:
                passed += 1
            else:
                failed += 1            
    print("three tone filter test:", passed, "pixels passed,", failed, "pixels failed")


#extreme contrast filter test- Joey Murphy
def test_extreme_contrast(file: str or Image) -> str:
    """Tests that an image, of the user's choosing, (passed through
    the extreme_contrast filter) contains RGB components of 255 if the component
    is greater then 127 or 0 if less then or equal to 127.
    """
   
    function = extreme_contrast(test)

    for pixels in function:
        x, y, (xtreme_r, xtreme_g, xtreme_b) = pixels
        (r, g, b) = get_color(function, x, y)
        
        if r >127 and xtreme_r != 255:
            return print("Test has failed.")
            
        elif r <= 127 and xtreme_r != 0:
            return print("Test has failed.")
            
        if g >127 and xtreme_g != 255:
            return print("Test has failed.")
        
        elif g <= 127 and xtreme_g != 0:
            return print("Test has failed.")
        
        if b >127 and xtreme_b != 255:
            return print("Test has failed.")
            
        elif b <= 127 and xtreme_b != 0:
            return print("Test has failed.")
                 
    else:
        return print("Test has passed!")


#sepia tinting filter test- Nguyen Gia Hieu Tu
def test_sepia():  
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(62, 62, 62))
    set_color(original, 2, 0,  create_color(63, 63, 63))
    set_color(original, 3, 0,  create_color(191, 191, 191))
    set_color(original, 4, 0,  create_color(192, 192, 192))
    set_color(original, 5, 0,  create_color(255, 255, 255))
       
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(62 * 1.1, 62, 62 * 0.9))
    set_color(expected, 2, 0,  create_color(63 * 1.15, 63, 63 * 0.85))
    set_color(expected, 3, 0,  create_color(191 * 1.15, 191, 191 * 0.85))
    set_color(expected, 4, 0,  create_color(192 * 1.08, 192, 192 * 0.93))
    set_color(expected, 5, 0,  create_color(255 * 1.08, 255, 255 * 0.93))
   

    sepia_tint = tinting(original)
    for x, y, col in sepia_tint:                                
                                
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))   
           

#posterizing filter test - Nguyen Gia Hieu Tu
def test_posterize(posterized) -> None:
    """Print a passed message if filtered_image matches expected for posterize  
    with every pixel. Otherwise, return an error message that includes the pixel 
    location(s) and colour(s) that failed the test."""
    print("Testing posterize")
    errors = []
    
    sample = create_image(4, 1)
    set_color(sample, 0, 0, create_color(25, 31, 95))
    set_color(sample, 1, 0, create_color(67, 0, 159))
    set_color(sample, 2, 0, create_color(180, 255, 223))
    set_color(sample, 3, 0, create_color(240, 191, 127))
    
    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(31, 31, 95))
    set_color(expected, 1, 0, create_color(95, 31, 159))
    set_color(expected, 2, 0, create_color(159, 223, 223))
    set_color(expected, 3, 0, create_color(223, 159, 95))    
    
    for pixel in sample:
        x, y, color = pixel
        if color != get_color(expected, x, y):
            errors.append((x, y))
    if len(errors) == 0:
        print("Passed test.")
    elif len(errors) == 1:
        print("Pixel", errors[0], "RGB", get_color(sample, errors[0][0], errors[0][1]), "does not match expected.")
    else:
        print("Pixels", errors, "do not match expected. RGB values are: ", end='')
        for err in errors:
            print(get_color(sample, err[0], err[1]), end=' ')
            

#vertical flip filter test - Adam Koziak
def vertical_test(original, flipped):
    width = get_width(original)
    passed = 0
    failed = 0
    for pixel in original:
        x, y, (r, g, b) = pixel
        r2, g2, b2 = get_color(flipped, (width-x-1), y)
        if (r, g, b) == (r2, g2, b2):
            passed += 1
        else:
            failed += 1
    print("vertical flip filter test:", passed, "pixels passed,", failed, "pixels failed")


#horizontal flip filter test - Joey Murphy
def flip_horizontal_test(s: Image) -> str:
    """ Test if the pixels in the first created image (passed through
    the flip_horizontal filter) are the same as the expected pixels in the
    second created image.
    """
    
    image = create_image(1, 4)
    set_color(image, 0, 0, create_color(58, 95, 67))
    set_color(image, 0, 1, create_color(24, 72, 90))
    set_color(image, 0, 2, create_color(87, 65, 31))
    set_color(image, 0, 3, create_color(93, 57, 32))
    
    expected_image = create_image(1, 4)
    set_color(expected_image, 0, 0, create_color(93, 57, 32))
    set_color(expected_image, 0, 1, create_color(87, 65, 31))
    set_color(expected_image, 0, 2, create_color(24, 72, 90))
    set_color(expected_image, 0, 3, create_color(58, 95, 67))
    
    flipped_pic = flip_horizontal(image)
    
    for x, y, (r, g, b) in flipped_pic:
        if get_color(flipped_pic, x, y) != get_color(expected_image, x, y):
            return print("Test has failed at x:", x, ", y:", y)
    return print("Test has passed.")


#edge detection filter test- Henry Lin
def test_edge(THRESHOLD) -> None:
    """Print a passed message if filtered_image matches expected for detect_edges  
    with every pixel using the given threshold value. Otherwise, return an error 
    message that includes the pixel location(s) and colour(s) that failed the test.
    """
    print("Testing detect_edges with threshold value", THRESHOLD)
    WHITE = create_color(255, 255, 255)
    BLACK = create_color(0, 0, 0)    
    errors = []
    threshhold = 20
    sample = create_image(2, 2)
    set_color(sample, 0, 0,  create_color(30, 60, 90))
    set_color(sample, 1, 0,  create_color(100, 255, 170))
    set_color(sample, 0, 1,  create_color(55, 60, 58))
    set_color(sample, 1, 1,  create_color(0, 0, 0))
    
    expected = copy(sample)
    lowest_pixel = 1    # get_height(expected) - 1
    
    for x, y, (r, g, b) in expected:
        if y < lowest_pixel:
            brightness = (r + g + b)/3
            below = get_color(expected, x, y + 1)
            brightness_below = (below[0] + below[1] + below[2])/3
            contrast = abs(brightness - brightness_below)
            if contrast > THRESHOLD:
                set_color(expected, x, y, BLACK)
            else: # contrast < THRESHOLD
                set_color(expected, x, y, WHITE)
        else: # y == lowest_pixel
            set_color(expected, x, y, WHITE)
    
    filtered_image = detect_edges(sample, threshhold)
    for x, y, color in filtered_image:
        if color != get_color(expected, x, y):
            errors.append((x, y))
    if len(errors) == 0:
        print("Passed test.")
    elif len(errors) == 1:
        print("Pixel", errors[0], "RGB", get_color(filtered_image, errors[0][0], errors[0][1]), "does not match expected.")
    else:
        print("Pixels", errors, "do not match expected. RGB values are: ", end='')
        for err in errors:
            print(get_color(filtered_image, err[0], err[1]), end=' ')


#improved edge detection filter test - Nguyen Gia Hieu Tu
def test_detect_edges():
    '''print PASSED if the sample image matches the expected image, print FAILED if the sample imgae does not match the expected image
    '''
    sample = create_image(2, 2)
    set_color(sample, 0, 0,  create_color(1, 2, 3))
    set_color(sample, 1, 0,  create_color(62, 62, 62))
    set_color(sample, 0, 1,  create_color(63, 63, 63))
    set_color(sample, 1, 1,  create_color(63, 63, 63))
    
    expected = create_image(2, 2)
    set_color(expected, 0, 0, create_color(0,0,0))
    set_color(expected, 1, 0, create_color(255, 255, 255))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 1, create_color(255, 255, 255))
            
    image = detect_edges_better (sample, 6)
    for x, y, col in image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                        col, get_color(expected, x, y))    
        


#testing script - Adam Koziak

original = load_image("p2-original.jpg")

red = red_channel(original)
test_red_channel(red)

green = green_channel(original)
test_green_channel(green)

blue = blue_channel(original)
test_blue_channel(blue)

combined = combine(red, green, blue)
test_combine(original, combined)

choice1 = "magenta"
choice2 = "cyan"
filtered = two_tone(original, choice1, choice2)
two_tone_test(original, filtered, choice1, choice2)

choice1 = "magenta"
choice2 = "cyan"
choice3 = "yellow"
filtered = three_tone(original, choice1, choice2, choice3)
three_tone_test(original, filtered, choice1, choice2, choice3)

test = extreme_contrast(original)
test_extreme_contrast(extreme_contrast(test))

sepia_image = tinting(original)
test_sepia()

posterized = posterize(original)
test_posterize(posterized)

flipped = flip_vertical(original)
vertical_test(original, flipped)

test = flip_horizontal(original)
flip_horizontal_test(flip_horizontal(test))

threshhold = 20
detect_edges(original, threshhold)
test_edge(20)

test_detect_edges()