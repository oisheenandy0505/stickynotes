import tkinter as tk
from tkinter import simpledialog, messagebox

class StickyNote:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Notes")
        
        # Set pale yellow background and black text color
        self.text_area = tk.Text(self.root, bg="#FFFFE0", fg="black", font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New Note", command=self.new_note)
        self.file_menu.add_command(label="Save Note", command=self.save_note)
        self.file_menu.add_command(label="Close", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.root.geometry("300x300")

    def new_note(self):
        self.text_area.delete(1.0, tk.END)

    def save_note(self):
        note_content = self.text_area.get(1.0, tk.END)
        with open("sticky_note.txt", "w") as file:
            file.write(note_content)
        messagebox.showinfo("Save Note", "Note saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    sticky_note = StickyNote(root)
    root.mainloop()
