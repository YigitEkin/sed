from PIL import Image

def crop_image(image_path, x, y):
    # Open the image
    image = Image.open(image_path)

    # Calculate the crop coordinates
    left = x
    upper = y
    right = x + 256
    lower = y + 256

    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))

    # Save the cropped image
    cropped_image.save('cropped_image.png')

# Example usage
image_path = 'sed_images/KyokugenCyclone.png'
x_start = 300
y_start = 40

crop_image(image_path, x_start, y_start)