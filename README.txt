Contact information: 
Adam Koziak 
101140761
adamkoziak@cmail.carleton.ca


Date: 
07/04/2020


Software: 
Name: Photo Editor 
Version: 1.0
Price: Free to use


Description: 
This application allows users to choose an image and apply different filters. There are 9 filters in total. The image can then be saved as a copy.

Installation: 
Required to install Python version 3 or above. Download and install from: https://www.python.org/downloads/windows
After installation, add Python 3 to PATH

Required to install Pillow. Download and install by typing python -m pip install Pillow into the command line. After Pillow is installed, type python -m pip install --upgrade pip to update pillow to the newest version.

Make sure all photo editor files are in the same directory


Usage: 
Two ways to start the program:
Use shell command by entering ‘cmd’ in the search bar on your window, prompt:
> python t85_interactive_ui.py
When prompted, enter users’ choices

Alternatively, if you have .py files set to open with Python by default, double click the file python t85_interactive_ui.py and it should run if installed correctly.
The command prompt should appear and text will guide the user through the program.
The interface will look like this:

Cimpl 1.04; October 6, 2017

L)oad image  S)ave as
2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
Q)uit

Type the character beside the option you would like to choose, and then press Enter.
Before you use any of the filters, you must first load an image by entering “L” in the command prompt and pressing Enter (capitals do not matter).
A window will appear that allows you to select an image file. The program will work with .jpg and .png files, however .png is recommended as there is no lossy compression when saving the image.
After you have selected your image, you may now use one of the filter options. Type the character beside the filter you would like to use and press Enter. For example, “E” for edge detect filter. The program will now filter the image and display it; wait until it finishes before proceeding.
If you are done filtering the image, you can save it by using the S)ave option. It will prompt you to enter a name to save it under. You can also filter the image further if you wish.
If at any time you would like to exit the program, enter “q” into the command prompt. This will discard any unsaved modifications to your image (the original file will be unchanged).

Using the batch mode:
Batch mode is intended to perform many operations on multiple files at once. It speeds up the process compared to going through the interactive interface for each file.
In order to use the batch mode, create a text file in the installation directory. In the file, each line represents a job to perform on a single image. The format of each job is as follows:
name-of-file name-to-saveas operations
Each parameter is separated with a single space. The name of the file is first, and must include the file extension (e.g. .jpg or .png). The name to save as must also include the file extension. The operations are the corresponding characters that would be entered in the interactive interface, in order of execution, each separated by a space. An example job is shown below:
original.png new.png P V
This job would take the image original.png, apply the P)osterize filter and then perform a V)ertical flip, then save the filtered image as a new file called new.png in the same directory.
Any number of jobs can be performed by putting each one on a new line. All images to be worked on must be moved to the installation directory first. Then, simply run the t85_batch_ui.py file using one of the methods mentioned above.
It will prompt the user to select a file. Choose the text file that contains the jobs. Then, simply wait for the jobs to finish. Once it is complete, the command prompt should close and all of the new files will be found in the directory.


Credit:
Joey Murphy
* Blue Filter and test
* Extreme Contrast Filter
* Two Tone test
* Three tone test
* Horizontal Flip Filter
* Vertical Flip test

Nguyen Gia Hieu Tu
* Green filter
* Green filter test
* Sepia tinting filter
* Posterizing test
* Edge detection filter
* Improved edge detection test

Henry Lin 
* Red Filter and test
* Posterizing Filter
* Sepia tinting filter test
* Improved edge detection filter
* Edge detection test

Adam Koziak
* Combine filter
* Combine filter test
* Two-tone filter
* Three-tone filter
* Extreme contrast filter test
* Vertical flip filter
* Horizontal flip test
* Testing script
* Batch UI
* Interactive UI
* Reworked:
   * Red filter
   * Red filter test
   * Blue filter
   * Blue filter test
   * Green filter
   * Green filter test


License: 
MIT License 
        Copyright (c) 2020 T85

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.