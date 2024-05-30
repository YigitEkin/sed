from PIL import Image

# List of image file paths
image_files = [
    "test_images_fig3/original/1_cropped.png",
    "test_images_fig3/downscaled/1_cropped.png",
    "test_images_fig3/results/patchgan/0.png",
    "test_images_fig3/results/patchgan_sed/0.png",
    "test_images_fig3/results/pixelwise/0.png",
    "test_images_fig3/results/pixelwise_sed/0.png",
]

# Open all the images
images = [Image.open(file) for file in image_files]

# Get the dimensions of the first image
width, height = images[0].size 

# Create a new blank image with the same dimensions
merged_image = Image.new("RGB", (width * 6, height))

# Paste each image onto the blank image
offset = 0
for image in images:
    merged_image.paste(image, (offset, 0))
    offset += width

# Save the merged image
merged_image.save("merged_image1.jpg")