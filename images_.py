from tkinter import *
from PIL import Image, ImageTk
import os
import random

def display_random_image():
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    print(f"Random number generated: {random_number}")

    # Construct the image path based on the random number
    image_path = f"C:\\Users\\AI-LAB\\Desktop\\images\\{random_number}.jpg"  # Change this path as needed

    # Check if the file exists
    if not os.path.exists(image_path):
        print("Image file does not exist.")
        return

    try:
        # Load the image
        image = Image.open(image_path)

        # Resize the image to 1920x1080
        image = image.resize((1920, 1080))

        # Convert the image to PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Update the label with the new image
        lol_label.config(image=photo)
        lol_label.image = photo  # Keep a reference to avoid garbage collection

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    global lol_label
    _root = Tk()
    _root.title("Random Image Viewer")

    # Set the window to fullscreen
    _root.attributes('-fullscreen', True)

    # Create a label to hold the image
    lol_label = Label(_root)
    lol_label.pack()

    # Create a button to generate and display a random image
    button = Button(_root, text="Show Random Image", command=display_random_image)
    button.pack()

    # Exit fullscreen on pressing the Escape key
    _root.bind("<Escape>", lambda e: _root.attributes('-fullscreen', False))

    _root.mainloop()

if __name__ == "__main__":
    main()