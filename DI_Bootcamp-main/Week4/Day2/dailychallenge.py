from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Load an image from the Flower Color Images dataset (replace 'path/to/image.jpg' with the actual image path)
image_path = 'path/to/image.jpg'
original_image = Image.open(image_path)

# Rotate the image by 90 degrees
rotated_image = original_image.rotate(90)

# Flip the image horizontally and then vertically
flipped_image = ImageOps.flip(ImageOps.mirror(original_image))

# Zoom in on the image (scale by 1.2x) using .resize()
zoomed_image = original_image.resize((int(original_image.width * 1.2), int(original_image.height * 1.2)))

# Function to display images side by side
def show_images(original, augmented, title):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(augmented)
    plt.title(title)
    plt.axis('off')

    plt.show()

# Display the original and augmented images side by side
show_images(original_image, rotated_image, 'Rotated Image by 90 degrees')
show_images(original_image, flipped_image, 'Flipped Horizontally and Vertically Image')
show_images(original_image, zoomed_image, 'Zoomed Image (1.2x)')
