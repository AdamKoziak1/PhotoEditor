import time
from Cimpl import *
from t85_image_filters import *

def choose_option():
    print("\nL)oad image  S)ave as")
    print("2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize")
    print("E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip")
    choice = (input("U)ndo  Q)uit\n\n: ")).lower()   
    return choice
    
choice = choose_option()

original = create_image(1, 1, (0,0,0))
post_filter = copy(original)

IMAGE_OPTIONS = ["2", "3", "x", "t", "p", "e", "i", "v", "h"]

image_chosen = False

while not image_chosen:
    if choice == "l":
        filename = choose_file()
        original = load_image(filename)
        post_filter = copy(original)
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

filtercount = 0
versions = [original]

endloop = False

while endloop == False:
    
    if choice == "l":
        filename = choose_file()
        original = load_image(filename)
        post_filter = copy(original)
        filtercount = 0
        versions = [original]        
        validchoice = True
        
    elif choice == "s":
        filename = input("Enter filename (name.png)\n\n: ")
        save_as(versions[filtercount], filename)
        print("Saved image")
        
    elif choice == "2":
        choices = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
        print("Please enter two of the following colors seperated by spaces\n", choices)               
        choice1, choice2 = (input("\n: ").split())
        post_filter = two_tone(versions[filtercount], choice1, choice2)
        
        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "3":
        choices = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
        print("Please enter three of the following colors seperated by spaces\n", choices)               
        choice1, choice2, choice3 = (input("\n: ").split())
        post_filter = three_tone(versions[filtercount], choice1, choice2, choice3)
        
        filtercount += 1
        versions.append(post_filter)
        show(post_filter)            
        
    elif choice == "x":
        post_filter = extreme_contrast(versions[filtercount])
        
        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "t":
        post_filter = tinting(versions[filtercount])

        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "p":
        post_filter = posterize(versions[filtercount])

        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "e":
        threshhold = int(input("Please enter threshhold\n\n: "))
        post_filter = detect_edges(versions[filtercount], threshhold)
        
        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "i":
        threshhold = int(input("Please enter threshhold\n\n: "))
        post_filter = detect_edges_better(versions[filtercount], threshhold)            
        
        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "v":
        post_filter = flip_vertical(versions[filtercount])
        
        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "h":
        post_filter = flip_horizontal(versions[filtercount])
        
        filtercount += 1
        versions.append(post_filter)
        show(post_filter) 
        
    elif choice == "u":
        if filtercount > 0:
            filtercount -= 1
            versions = versions[:-1]
            show(versions[filtercount])                
        else:
            print("Nothing to undo")
            
    elif choice == "q":
        endloop = True
        print("End of line.")
        time.sleep(1)
        exit()
        
    choice = choose_option()