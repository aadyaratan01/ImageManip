
from PIL import Image, ImageOps, ImageEnhance


def increase_brightness(image: Image):
    """Increase brightness by 10%
    This is equal to multiplying each row in the matrix by 1.10
    """

    # Get a list of tuples representing each pixel [(Red, Green, Blue), (Red, Green, Blue), ...]
    image_data = image.getdata()

    modified_image_data = []

    # Modify each component (Red, Green, and Blue) in every pixel
    for pixel in image_data:
        pixel = [int(component * 1.10) for component in pixel]

        modified_image_data.append(tuple(pixel))

    modified_image = Image.new(mode="RGB", size=image.size)

    modified_image.putdata(modified_image_data)

    return modified_image


def make_negative(image: Image):
    """Make image negative in color
    This is equal to subtracting two matrices [(Red, Green, Blue), ...] from [(255, 255, 255), ...]
    """

    # Get a list of tuples representing each pixel [(Red, Green, Blue), (Red, Green, Blue), ...]
    image_data = image.getdata()

    modified_image_data = []

    # Modify each component (Red, Green, and Blue) in every pixel
    for pixel in image_data:
        pixel = [255 - component for component in pixel]

        modified_image_data.append(tuple(pixel))

    modified_image = Image.new(mode="RGB", size=image.size)

    modified_image.putdata(modified_image_data)

    return modified_image


def add_border(image: Image):
    """Add a black border of width 10px"""
    border_width = 10
    border_color = "black"

    return ImageOps.expand(image, border=border_width, fill=border_color)


def enhance_image(image: Image):
    """Enhance image color"""

    return ImageEnhance.Color(image).enhance(2.0)


def invalid_choice(image: Image):
    print("Invalid choice, source image will be shown")

    return image


image = Image.open(input("Enter image path: ")).convert("RGB")

choices = {
    1: increase_brightness,
    2: make_negative,
    3: skew_image,
    4: crop_and_resize,
    5: add_border,
    6: enhance_image,
}

choice = int(
    input(
        "Enter:\n\n1. To increase brightness by 10%\n2. To make image negative in color\n3. To skew image\n4. To crop and resize image\n5. To add border\n6. To enhance image\n\n:"
    )
)

image = choices.get(choice, invalid_choice)(image)

image.show()
