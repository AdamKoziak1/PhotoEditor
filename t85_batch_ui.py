'''
Milestone 3
Group 85
31/03/2020
Adam Koziak
'''

from Cimpl import *
from t85_image_filters import *

batch = open("batch_sample.txt", "r")

lines = []

filename = ""
saveas = ""
filters = []


THRESHHOLD = 10

for line in batch:
    lines.append(line.split())
    
for line in lines:
    filename = line[0].lower()
    del line[0]
    saveas = line[0].lower()
    del line[0]
    
    original = load_image(filename)
    filtered = copy(original)     
    
    for i in line:
        i = i.lower()
        if i == "2":
            choice1 = "yellow"
            choice2 = "cyan"
            filtered = two_tone(filtered, choice1, choice2)
            
        elif i == "3":
            choice1 = "yellow"
            choice2 = "magenta"
            choice3 = "cyan"
            filtered = three_tone(filtered, choice1, choice2, choice3)
            
        elif i == "x":
            filtered = extreme_contrast(filtered)
            
        elif i == "t":
            filtered = tinting(filtered)
            
        elif i == "p":
            filtered = posterize(filtered)
            
        elif i == "e":
            filtered = detect_edges(filtered, THRESHHOLD)
            
        elif i == "i":
            filtered = detect_edges_better(filtered, THRESHHOLD)
            
        elif i == "v":
            filtered = flip_vertical(filtered)
            
        elif i == "h":
            filtered = flip_horizontal(filtered)
    save_as(filtered, saveas)