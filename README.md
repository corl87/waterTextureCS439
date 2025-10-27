# waterTextureCS439

the main goal of this project was to make a wave effect using lower level graphics manipulation. The wave is made with "lines" which have a set thickness of 1 pixel. 
The way this is accomplished is by taking sine of time and adding offset, to illustrate the full wave and not just one segment. Inspiration comes from the sine of time godot shader demonstration in class.

I am most comforatble with python so I chose to make this illustration in pygame. I understand that there are multiple levels below pygame in abstraction, yet i wanted to create something more interesting than a still image so I opted to go with what I knew. I believe I acheived this goal with my wave simulation. 

Even though I used a platform I was most comforable with, I still learned some new concepts. At the start of this project I used RGB values to represent my colors because I understood them, but I soon got confused having 3 values represent 1 color parameter when drawing my lines. To curb this issue, I defined the color values as a tuple at the start of my code in order to improve readability. I had another issue with clarity when it came to keeping track of the tops and bottoms of the lines seperately, so I first defined the yCenter and then derived the tops and bottoms from its center. Also, actaully implementing the concept of sine time was suprisingly difficult despite it being outlined in class, due to there being multiple instances that needed different starting positions. 

In order to run my project you only need to run waveTek.py. It is advisable to open it in a python IDE of your choice and clicking run from there. It *should* be executable from command line as well. 
