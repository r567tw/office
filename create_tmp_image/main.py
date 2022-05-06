from PIL import Image  

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height) )
img.save('test.png')