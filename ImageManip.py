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
