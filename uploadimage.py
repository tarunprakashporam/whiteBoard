from tkinter import filedialog, PhotoImage
import os

def upload_image(canvas, elements, current_element):
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
)

    if file_path:
        if not os.path.isfile(file_path):
            print(f"Error: The selected file '{file_path}' is not a valid image file.")
            return elements, current_element

        try:
            image = PhotoImage(file=file_path)
            elements.append(image)
            current_element = image
            canvas.create_image(10, 10, anchor="nw", image=image)
        except Exception as e:
            print(f"Error loading image: {e}")

    return elements, current_element

