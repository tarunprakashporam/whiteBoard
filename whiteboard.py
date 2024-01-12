# whiteboardapp.py

import tkinter as tk
from tkinter import Canvas, simpledialog
from uploadimage import upload_image
from uploaddocument import upload_document
from insertsticky import insert_sticky_note
from text_box import insert_resizable_text_box  # Import the function
from previousandnext import HistoryManager
class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Whiteboard App")

        self.canvas = Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.elements = []  # To store text and image elements
        self.current_element = None  # To keep track of the current element
        self.history_manager = HistoryManager()  # For undo and redo

        # Undo Button
        self.undo_button = tk.Button(root, text="Undo", command=self.undo)
        self.undo_button.pack(side=tk.LEFT, padx=10)

        # Redo Button
        self.redo_button = tk.Button(root, text="Redo", command=self.redo)
        self.redo_button.pack(side=tk.LEFT, padx=10)

        # Insert Resizable Text Box Button
        self.text_box_button = tk.Button(root, text="Insert Resizable Text Box", command=self.insert_resizable_text_box)
        self.text_box_button.pack(side=tk.LEFT, padx=10)

        # Upload Image Button
        self.upload_image_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_image_button.pack(side=tk.LEFT, padx=10)

        # Upload Document Button
        self.upload_document_button = tk.Button(root, text="Upload Document", command=self.upload_document)
        self.upload_document_button.pack(side=tk.LEFT, padx=10)

        # Insert Sticky Note Button
        self.insert_sticky_button = tk.Button(root, text="Insert Sticky Note", command=self.insert_sticky_note)
        self.insert_sticky_button.pack(side=tk.LEFT, padx=10)

    def undo(self):
        state = self.history_manager.undo()
        if state:
            self.elements, self.current_element = state
            self.refresh_canvas()

    def redo(self):
        state = self.history_manager.redo()
        if state:
            self.elements, self.current_element = state
            self.refresh_canvas()

    def refresh_canvas(self):
        self.canvas.delete("all")
        for element in self.elements:
            # Draw the elements on the canvas
            pass


    def insert_resizable_text_box(self):
        self.elements, self.current_element = insert_resizable_text_box(self.canvas, self.elements, self.current_element)

    def upload_image(self):
        self.elements, self.current_element = upload_image(self.canvas, self.elements, self.current_element)

    def upload_document(self):
        self.elements, self.current_element = upload_document(self.canvas, self.elements, self.current_element)

    def insert_sticky_note(self):
        self.elements, self.current_element = insert_sticky_note(self.canvas, self.elements, self.current_element)

if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()

