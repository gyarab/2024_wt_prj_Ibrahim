import django
from PIL import Image
from PIL import Image

# Open an image file
img = Image.open("example.jpg")  # Replace with the path to an image file you have
img.show()  # This will open the image in the default viewer

# Optionally, resize and save the image
img_resized = img.resize((200, 200))
img_resized.save("resized_example.jpg")  # Saves the resized image
print("Image opened and resized successfully.")
