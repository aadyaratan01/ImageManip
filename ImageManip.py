from PIL import Image, ImageOps, ImageEnhance


def increase_brightness(source_image: Image):
    """Increase brightness by 10%
    This is equal to multiplying each row in the matrix by 1.10 (a scalar value)
    """

    # Get a list of tuples representing each pixel [(Red, Green, Blue), (Red, Green, Blue), ...]
    image_data = source_image.getdata()

    modified_image_data = []

    # Modify each component (Red, Green, and Blue) in every pixel
    for pixel in image_data:
        pixel = [int(component * 1.10) for component in pixel]

        modified_image_data.append(tuple(pixel))

    modified_image = Image.new(mode="RGB", size=source_image.size)

    modified_image.putdata(modified_image_data)

    return modified_image


def make_negative(source_image: Image):
    """Make image negative in color
    This is equal to subtracting two matrices [(Red, Green, Blue), ...] from [(255, 255, 255), ...]
    """

    # Get a list of tuples representing each pixel [(Red, Green, Blue), (Red, Green, Blue), ...]
    image_data = source_image.getdata()

    modified_image_data = []

    # Modify each component (Red, Green, and Blue) in every pixel
    for pixel in image_data:
        pixel = [255 - component for component in pixel]

        modified_image_data.append(tuple(pixel))

    modified_image = Image.new(mode="RGB", size=source_image.size)

    modified_image.putdata(modified_image_data)

    return modified_image


def skew_image(source_image: Image):
    # Skews an image

    skewed_image = source_image.copy()

    skewed_image = skewed_image.transform(
        skewed_image.size, Image.AFFINE, (1, -0.5, 0.5 * skewed_image.size[0], 0, 1, 0)
    )

    return skewed_image


def crop_and_resize(source_image: Image):
    """Crops and Resizes an Image
    This function helps to crop a part of the image and resize to whatever scale.
    The parameters are( measure of the final image, coordinates of top left corner, width and height)"""

    cropped_image = source_image.copy()

    cropped_image = cropped_image.transform(
        cropped_image.size,
        Image.EXTENT,
        (30, 40, cropped_image.size[0] * 5 // 6, cropped_image.size[1] // 2 + 40),
    )

    return cropped_image


def add_border(source_image: Image):
    """Add a black border of width 10px"""
    border_width = 10
    border_color = "black"

    return ImageOps.expand(source_image, border=border_width, fill=border_color)


def enhance_image(source_image: Image):
    """Enhance image color"""

    return ImageEnhance.Color(source_image).enhance(2.0)


def make_grayscale(source_image: Image):
    """Make image grayscale"""
    return ImageOps.grayscale(source_image)

def mirror_image(source_image: Image):
    width, height = source_image.size

    new_image = Image.new(mode="RGB", size=source_image.size)

    for x in range(width):
        for y in range(height):
            new_pixel = source_image.getpixel((width - x - 1, y))
            new_image.putpixel((x, y), new_pixel)

    return new_image
    
    
def invalid_choice(source_image: Image):
    print("Invalid choice, source image will be shown")

    return source_image


image = Image.open(input("Enter image path: ")).convert("RGB")

choices = {
    1: increase_brightness,
    2: make_negative,
    3: skew_image,
    4: crop_and_resize,
    5: add_border,
    6: enhance_image,
    7: make_grayscale,
    8: mirror_image
}

choice = int(
    input(
        "Enter:\n\n1. To increase brightness by 10%\n2. To make image negative in color\n3. To skew "
        "image\n4. To crop and resize image\n5. To add border\n6. To enhance image\n7. To make image black and "
        "white\n8. To mirror image\n: "
    )
)

image = choices.get(choice, invalid_choice)(image)

image.show()
