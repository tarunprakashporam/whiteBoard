from tkinter import simpledialog, Label

def insert_sticky_note(canvas, elements, current_element):
    note = simpledialog.askstring("Insert Sticky Note", "Enter note:")
    if note:
        # Set the desired location for the sticky note (e.g., at coordinates (100, 100))
        x, y = 100, 100

        note_label = Label(canvas, text=note, bg="yellow", padx=10, pady=5, wraplength=200)
        canvas.create_window(x, y, anchor="nw", window=note_label)
        elements.append(note_label)
        current_element = note_label

    return elements, current_element

