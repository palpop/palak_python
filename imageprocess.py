#Flipping the image
from PIL import Image

#opening the image
img=Image.open('YOUR-IMAGE.jpg')

#transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#save it to a output file
transposed_img.save('corrected.jpg')

print('Done Flipping') 
