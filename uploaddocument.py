# uploaddocument.py

from tkinter import filedialog, Text

def upload_document(canvas, elements, current_element):
    file_path = filedialog.askopenfilename(title="Select Document", filetypes=[("Document files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            document_text = file.read()

        text_widget = Text(canvas, font=("Arial", 12), wrap="word", width=40, height=10)
        text_widget.insert("end", document_text)
        x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
        canvas.create_window(x, y, anchor="nw", window=text_widget)
        elements.append(text_widget)
        current_element = text_widget

    return elements, current_element

