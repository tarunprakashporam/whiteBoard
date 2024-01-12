import tkinter as tk
from tkinter import simpledialog, Text

TEXT_BOX_SETTINGS = {
    "font": ("Arial", 12),
    "wrap": tk.WORD,
    "width": 20,
    "height": 5
}

class ResizableTextBox:
    def __init__(self, canvas, x, y, initial_text=""):
        self.canvas = canvas
        self.text_widget = Text(self.canvas, **TEXT_BOX_SETTINGS)
        self.text_widget.insert(tk.END, initial_text)

        self.rect = self.canvas.create_rectangle(x, y, x + self.text_widget.winfo_reqwidth(),
                                                 y + self.text_widget.winfo_reqheight(), outline="black")
        self.canvas.create_window(x, y, anchor=tk.NW, window=self.text_widget)

        self.start_x = 0
        self.start_y = 0
        self.is_resizing = False

        self.canvas.tag_bind(self.rect, "<Button-1>", self.start_resize)
        self.canvas.tag_bind(self.rect, "<B1-Motion>", self.resize)
        self.canvas.tag_bind(self.rect, "<ButtonRelease-1>", self.stop_resize)

    def start_resize(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.is_resizing = True

    def resize(self, event):
        if self.is_resizing:
            new_width = event.x - self.start_x
            new_height = event.y - self.start_y

            # Ensure minimum width and height
            new_width = max(new_width, 50)
            new_height = max(new_height, 50)

            # Update rectangle and text widget sizes proportionally
            self.canvas.coords(self.rect, self.start_x, self.start_y, self.start_x + new_width, self.start_y + new_height)
            self.text_widget.config(width=new_width, height=new_height)

            # Optional: Provide visual feedback during resizing
            # self.canvas.itemconfig(self.rect, outline="red", width=2)  # Highlight border

    def stop_resize(self, event):
        self.is_resizing = False
        # Optional: Remove visual feedback after resizing
        # self.canvas.itemconfig(self.rect, outline="black", width=1)

def insert_resizable_text_box(canvas, elements, current_element):
    text = simpledialog.askstring("Insert Resizable Text Box", "Enter text:")
    if text:
        resizable_text_box = ResizableTextBox(canvas, 50, 50, text)
        elements.append(resizable_text_box)
        current_element = resizable_text_box

    return elements, current_element

