from PIL import Image


def alter_brightness(pixel, level):
    """Alter RGB brightness level
    This is equal to multiplying each row in the matrix by level
    """
    pixel = [int(component * level) for component in pixel]

    return tuple(pixel)


image = Image.open(input("Enter image path: ")).convert("RGB")

# Get a list of tuples representing each pixel [(Red, Green, Blue), (Red, Green, Blue), ...]
image_data = image.getdata()

# Modify each pixel's RGB value
image_data_modified = [alter_brightness(pixel, 1.15) for pixel in image_data]

# Create a new temporary image
new_image = Image.new(mode="RGB", size=image.size)

# Copy the modified pixel data onto new image
new_image.putdata(image_data_modified)

# Show the newly generated image
new_image.show()

from PIL import Image 

#Skews an image--function 1
Image1 = Image.open('cat.jpg')
Image1 = Image1.transform(Image1.size,Image.AFFINE,(1,-0.5,0.5 * Image1.size[0],0,1,0))
Image1.save('cat_skewed.jpg')

#Extents an Image--Function 2
# This function helps to crop a part of the image and resize to whaterver scale. the parameters are( measure of the final image, coordinates of top left corner, width and height)
Image2 = Image.open('cat.jpg')
print(Image2.size)
Image2 = Image2.transform(Image2.size,Image.EXTENT,(30,40,Image2.size[0]*5//6,Image2.size[1]//2+40))
Image2.save('cat_crop&zoom.jpg')
