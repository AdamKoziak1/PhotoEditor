'''
Milestone 3
Group 85
31/03/2020
Adam Koziak
'''

import time
from Cimpl import *
from t85_image_filters import *

def choose_option(): 
    '''
    prints the options of the program, and prompts user to enter their choice. function returns choice.
    '''
    print("\nL)oad image  S)ave as")
    print("2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize")
    print("E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip")
    choice = (input("Q)uit\n\n: ")).lower()   
    return choice
    
choice = choose_option()

original = create_image(1, 1, (0,0,0))
filtered = copy(original)

IMAGE_OPTIONS = ["2", "3", "x", "t", "p", "e", "i", "v", "h"]

THRESHHOLD = 10

image_chosen = False

while not image_chosen:
    '''
    loop makes sure an image is loaded before you can proceed with any options
    '''
    if choice == "l":
        filename = choose_file()
        original = load_image(filename)
        filtered = copy(original)
        image_chosen = True
        
    elif choice == "q":
        print("End of line.")
        time.sleep(1)
        exit()
        
    elif choice in IMAGE_OPTIONS:
        choice = input("No image loaded\n\n: ").lower()
        
    else:
        choice = input("No such command\n\n: ").lower()        


choice = choose_option()

endloop = False

while endloop == False:
    '''
    loop allows user to select filters and executes filter on current version of image.
    '''
    if choice == "l":
        filename = choose_file()
        original = load_image(filename)
        filtered = copy(original) 
        validchoice = True
        
    elif choice == "s":
        filename = input("Enter filename (name.png)\n\n: ")
        save_as(filtered, filename)
        print("Saved image")
        
    elif choice == "2":
        '''
        choices = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
        print("Please enter two of the following colors seperated by spaces\n", choices)               
        choice1, choice2 = (input("\n: ").split())
        '''
        choice1 = "yellow"
        choice2 = "cyan"        
        filtered = two_tone(filtered, choice1, choice2)
        show(filtered) 
        
    elif choice == "3":
        '''
        choices = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
        print("Please enter three of the following colors seperated by spaces\n", choices)               
        choice1, choice2, choice3 = (input("\n: ").split())
        '''
        choice1 = "yellow"
        choice2 = "magenta"
        choice3 = "cyan"        
        filtered = three_tone(filtered, choice1, choice2, choice3)
        show(filtered)            
        
    elif choice == "x":
        filtered = extreme_contrast(filtered)
        show(filtered) 
        
    elif choice == "t":
        filtered = tinting(filtered)
        show(filtered) 
        
    elif choice == "p":
        filtered = posterize(filtered)
        show(filtered) 
        
    elif choice == "e":
        #threshhold = int(input("Please enter threshhold\n\n: "))
        filtered = detect_edges(filtered, THRESHHOLD)
        show(filtered) 
        
    elif choice == "i":
        #threshhold = int(input("Please enter threshhold\n\n: "))
        filtered = detect_edges_better(filtered, THRESHHOLD)
        show(filtered) 
        
    elif choice == "v":
        filtered = flip_vertical(filtered)
        show(filtered) 
        
    elif choice == "h":
        filtered = flip_horizontal(filtered)
        show(filtered) 
        
    elif choice == "q":
        endloop = True
        print("End of line.")
        time.sleep(1)
        exit()
        
    else:
        print("No such command")
        
    choice = choose_option()