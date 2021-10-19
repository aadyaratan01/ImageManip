from PIL import Image


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


def invalid_choice(image: Image):
    print("Invalid choice, source image will be shown")

    return image


image = Image.open(input("Enter image path: ")).convert("RGB")

choices = {1: increase_brightness, 2: make_negative, 3: skew_image, 4: crop_and_resize}

choice = int(
    input(
        "Enter:\n1. To increase brightness by 10%\n2. To make image negative in color\n3. To skew image\n 4. To crop and resize image\n:"
    )
)

image = choices.get(choice, invalid_choice)(image)

image.show()
